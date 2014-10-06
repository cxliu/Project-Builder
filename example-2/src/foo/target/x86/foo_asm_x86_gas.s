.data
LC0:
    .ascii "foo_asm_x86_gas.s was called\n\0"
.text
    .global foo_asm
foo_asm:
    pushl    %ebp
    movl    %esp, %ebp
    subl    $4, %esp
    movl    $LC0, (%esp)
    call    printf
    movl    $0, %eax
    leave
    ret
