extern GetStdHandle
extern WriteFile
extern ExitProcess

section .rodata

msg db "Hello World!", 0x0d, 0x0a

msg_len equ $-msg
stdout_query equ -11

section .data

stdout dw 0
bytes_written dw 0

section .text

global start

start:
    mov rcx, stdout_query
    call GetStdHandle
    mov [rel stdout], rax

    mov  rcx, [rel stdout]
    mov  rdx, msg
    mov  r8, msg_len
    mov  r9, bytes_written
    push qword 0
    call WriteFile

    xor rcx, rcx
    call ExitProcess

section .customlongnamesection
    test_data db "This is a custom long name section", 0x0d, 0x0a

section .someothersection
    func:
        ret

section .longsec1
    func1:
        mov rax, 0
        ret

section .longsec2
    func2:
        mov rax, 0
        ret

section .longsec3
    func3:
        mov rax, 0
        ret

section .longsec4
    func4:
        mov rax, 0
        ret

section .longsec5
    func5:
        mov rax, 0
        ret

section .longsec6
    func6:
        mov rax, 0
        ret

section .longsec7
    func7:
        mov rax, 0
        ret

