# This module is a holder of some helper utilities which seek to give better error 
# messages when things go wrong. Sometimes it may break abstraction a little bit 
# to poke around inside the m2 internals, and the interfaces may change without
# much thought.

import m2

def what_sets_this_attribute(manifest, attribute):
	"""Given an attribute name, return a list of all the attribute outcomes that
	set the attribute.
	"""
	ret = []
	for c in manifest._clauses:
		values = c.get_attribute_dict(ignore_errors=True)
		if attribute in values:
			for outcome in values[attribute]:
				ret.append(outcome)
	
	return ret

def what_adds_this_keyword(manifest, keyword):
	"""Given a keyword, return a list of all the clauses and positions that add it."""
	ret = []
	for c in manifest._clauses:
		implications = c.get_implies(ignore_errors=True)
		for imp, pos in implications:
			if imp == keyword:
				ret.append((c, pos))

	return ret

def get_expanded_keywords(manifest, starting_keywords):
	"""Given a set of starting keywords, return a list of expanded keywords.
	"""
	files, attribs, keys = manifest._clauses.solve(starting_keywords, ignore_errors=True)
	return keys

def why_is_this_keyword_set(manifest, keyword, starting_keywords):
	"""Given a set of starting keywords, return a list of clauses
	which lead to a specific keyword being set.
	"""
	ret = []
	expanded_keywords = get_expanded_keywords(manifest, starting_keywords)
	if keyword in starting_keywords:
		# Too easy
		reason = "keyword %s is already in the starting keywords [%s]!" % (keyword, ' '.join(sorted(starting_keywords)))
		ret.append((reason, "", "", ""))
		return ret

	if not keyword in expanded_keywords:
		# Wrong request
		reason = "keyword %s is not in the expanded keywords [%s]!" % (keyword, ' '.join(sorted(expanded_keywords)))
		ret.append((reason, "", "", ""))
		return ret

	# Get a list of clauses that will set the queried keyword
	for c in manifest._clauses:
		implications = c.get_implies(ignore_errors=True)
		if implications:
			for (kw,ps) in implications:
				if keyword in kw:
					if c.satisfied(expanded_keywords):
						ret.append(("", keyword, c, ps))

	# Check the list of clauses for direct clauses
	# a direct clause is a clause which is already satisfied using the starting_keywords
	direct_clauses = []
	for (reason, kw, c, pos) in ret:
		if c.satisfied(set(starting_keywords)):
			direct_clauses.append((reason, kw, c, pos))
	if direct_clauses:
        # if we have direct clauses, we just return them and not all clauses
		return direct_clauses
	else:
		# we do not have a direct clause
		# either return all clauses or try to pick the first and do a recursive call
		reason, kw, c, pos = ret[0]
		assert isinstance(c, m2.Clause)
		c_kw_exp = c.get_keyword_expression()
		if not c_kw_exp.contains_or():
			new_keywords = c_kw_exp.get_keywords()
			if len(new_keywords) == 1:
				new_keyword = new_keywords.pop()
				ret = []
				# start with picked clause
				ret.append((reason, kw, c, pos))
				# recursive call using new_keyword
				for reason, kw, c, pos in why_is_this_keyword_set(manifest, new_keyword, starting_keywords):
					ret.append((reason, kw, c, pos))
		return ret

def how_did_this_attribute_get_its_value(manifest, attribute, keywords):
	"""Given an attribute name and a set of keywords, return a list of
	attribute outcomes that were considered for the value of this attribute.
	"""
	ret = []
	files, attribs, keys = manifest._clauses.solve(keywords, ignore_errors=True)
	for a in attribs:
		if a.get_key() == attribute:
			ret.append(a)
	
	return ret
