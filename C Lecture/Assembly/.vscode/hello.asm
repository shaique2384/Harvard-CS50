global _start

section .text
_start:
    ; write(1, msg, len)
    mov rax, 1          ; system call for write
    mov rdi, 1          ; file descriptor 1 is stdout
    mov rsi, msg        ; pointer to string
    mov rdx, len        ; length of string
    syscall             ; invoke operating system to write

    ; exit(0)
    mov rax, 60         ; system call for exit
    xor rdi, rdi        ; return code 0
    syscall             ; invoke operating system to exit

section .data
    msg db "Hello, World!", 10    ; 10 is the newline character (\n)
    len equ $ - msg               ; calculate string length