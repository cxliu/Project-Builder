from xml.etree.ElementTree import *
from xml.etree.ElementTree import _encode, _raise_serialization_error
from xml.etree import ElementTree as _ElementTree
import string

class ElementTree(_ElementTree.ElementTree):

	def write(self, file, encoding="utf-8"):
		assert self._root is not None
		# ensure file is not null
		if not hasattr(file, "write"): 
			file = open(file, "wb")
		
		if encoding == "utf-8":
			file.write("\357\273\277") # UTF-8 Unicode (BOM) indication
		
		file.write("<?xml version=\"1.0\" encoding=\"%s\"?>" % encoding)
		self._indent = 0
		self._write(file, self._root, encoding, {})
		file.write("\n")

	def _write(self, file, node, encoding, namespaces):
		# write XML to file
		tag = node.tag
		if tag is Comment:
			file.write("\n<!-- %s -->" % _escape_cdata(node.text, encoding))
		elif tag is ProcessingInstruction:
			file.write("\n<?%s?>" % _escape_cdata(node.text, encoding))
		else:
			items = node.items()
			xmlns_items = [] # new namespaces in this scope
			try:
				if isinstance(tag, QName) or tag[:1] == "{":
					tag, xmlns = fixtag(tag, namespaces)
					if xmlns: 
						xmlns_items.append(xmlns)
			except TypeError:
				_raise_serialization_error(tag)
			
			file.write("\n" + "\t"*self._indent + "<%s" % (_encode(tag, encoding)))
			
			self._indent += 1
			if items or xmlns_items:
				items.sort() # lexical order
				for k, v in items:
					try:
						if isinstance(k, QName) or k[:1] == "{":
							k, xmlns = fixtag(k, namespaces)
							if xmlns: 
								xmlns_items.append(xmlns)
					except TypeError:
						_raise_serialization_error(k)
					
					try:
						if isinstance(v, QName):
							v, xmlns = fixtag(v, namespaces)
							if xmlns:
								xmlns_items.append(xmlns)
					except TypeError:
						_raise_serialization_error(v)
					
					file.write("\n" + "\t"*self._indent + "%s=\"%s\"" % \
					(_encode(k, encoding), _escape_attrib(v, encoding)))
				for k, v in xmlns_items:
					file.write("\n" + "\t"*self._indent + "%s=\"%s\"" % \
					(_encode(k, encoding), _escape_attrib(v, encoding)))
			
			
			if(node.text or len(node)):
				if (items or xmlns_items):
					file.write("\n" + "\t"*self._indent + ">")
				else:
					file.write(">")
			self._indent -= 1
			
			if node.text or len(node):
				if node.text:
					file.write(_escape_cdata(node.text, encoding))
				for n in node:
					self._indent += 1
					self._write(file, n, encoding, namespaces)
					self._indent -= 1
				file.write("\n" + "\t"*self._indent + "</" + _encode(tag, encoding) + ">")
			else:
				file.write("\n" + "\t"*self._indent + "/>")
			
			for k, v in xmlns_items:
				del namespaces[v]
			
		if node.tail:
			file.write(_escape_cdata(node.tail, encoding))
		


def _escape_attrib(attr_val, encoding=None, replace=string.replace):
	# escape attribute value
	text = str(attr_val)
	try:
		if encoding:
			text = _encode(text, encoding)
		text = replace(text, "&", "&amp;")
		#text = replace(text, "'", "&apos;") # FIXME: overkill
		text = replace(text, "\"", "&quot;")
		text = replace(text, "<", "&lt;")
		text = replace(text, ">", "&gt;")
		return text
	except (TypeError, AttributeError):
		_raise_serialization_error(text)

def _escape_cdata(text, encoding=None, replace=string.replace):
	try:
		if encoding:
			text = _encode(text, encoding)
		text = replace(text, "&", "&amp;")
		text = replace(text, "<", "&lt;")
		text = replace(text, ">", "&gt;")
		return text
	except (TypeError, AttributeError):
		_raise_serialization_error(text)


def tostring(element, encoding=None):
	class dummy:
		pass
	data = []
	file = dummy()
	file.write = data.append
	ElementTree(element).write(file, encoding)
	return string.join(data, "")
