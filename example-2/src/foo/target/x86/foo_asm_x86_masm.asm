.386
.model flat, c

.data
message BYTE "foo_asm_x86_masm.asm was called",0dh,0ah,0

printf proto c :vararg
public foo_asm

.code
foo_asm PROC
	invoke printf,OFFSET message
    ret
foo_asm ENDP

end