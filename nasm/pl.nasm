%macro print 2
    push_d
    mov edx, %1
    mov ecx, %2
    mov ebx, 1
    mov eax, 4
    int 0x80
    pop_d
%endmacro

%macro push_d 0
    push eax
    push ebx
    push ecx
    push edx
%endmacro

%macro pop_d 0
    pop edx
    pop ecx
    pop ebx
    pop eax
%endmacro

%macro dprint 0
    push_d
    
    mov ecx, 10
    mov bx, 0
    
%%_divide:
    mov edx, 0
    div ecx
    push dx
    inc bx
    
    test eax, eax   ; побитовое сравнение
    
    jnz %%_divide
    
%%_out:
    pop ax
    add ax, '0'
    mov [result], ax
    
    print 1, result ; часто вызываем принт для цифры
    
    dec bx
    cmp bx, 0
    jnz %%_out

    ;print nlen, newline
    ;print len, message
    ;print nlen, newline
    
    pop_d
%endmacro

section .text
    global _start
    
    
_start:
    mov ebx, 0
    
_loop:
    add al, [array + ebx]
    
    inc ebx
    cmp ebx, alen
    jne _loop
    
    dprint

_end:
    mov ebx, 0
    mov eax, 1   ;sys_exit
    int 0x80    ;call kernel


section .bss
    result resb 1

section .data
    array db 10, 13, 14, 7, 8, 12
    alen equ $ - array
    number dd 3200
    message db "Done"
    len equ $ - message
    newline db 0xA, 0xD
    nlen equ $ - newline
