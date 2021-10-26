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
    
    test eax, eax
    
    jnz %%_divide
    
%%_out:
    pop ax
    add ax, '0'
    mov [result], ax
    
    print 1, result
    
    dec bx
    cmp bx, 0
    jnz %%_out
    
    pop_d
%endmacro

%macro array_sum 2
    push_d
    
    mov ecx, 0
%%_loop:
    add al, [%1 + ecx]
    inc ecx
    
    cmp ecx, %2
    jne %%_loop
    
    mov [result], al
    
    pop_d
%endmacro

%macro mean 2
    push_d
    
    array_sum %1, %2
    
    mov al, %2
    mov bl, 4
    div bl; dd size

    mov bl, al
    mov al, [result]
    div bl
    
    mov [result], al
    
    pop_d
%endmacro

%macro sdprint 0
    push_d

    print slen, sign
    
    mov bx, ax
    mov ax, 0x100
    sub ax, bx
    
    dprint

    pop_d
%endmacro

section .text
    global _start
    
    
_start:

    print len, message

    mean x, xlen
    mov al, [result]
    
    mean y, ylen
    sub al, [result]

    test al, 128
    je _unsigned
    
_signed:
    sdprint
    jmp _end
    
_unsigned:
    dprint

_end:
    mov ebx, 0
    mov eax, 1   ;sys_exit
    int 0x80    ;call kernel


section .bss
    result resb 1

section .data
    x dd 5, 3, 2, 6, 1, 7, 4
    xlen equ $ - x
    y dd 0, 10, 1, 9, 2, 8, 5
    ylen equ $ - y
    
    message db "Mean of the difference: "
    len equ $ - message
    
    sign db "-"
    slen equ $ - sign
    
    newline db 0xA, 0xD
    nlen equ $ - newline
