data segment
    MSG DB "enter a character:$"
    data ends

code segment
    assume cs:code,ds:data
    start:
    mov ax,data
    mov ds,ax
    lea dx,MSG
    mov ah,09h
    int 21h
    mov ah,01
    int 21h 
    mov ah,02 
    int 21h
    mov ah,4ch
    int 21h
    code ends
end start


ret




