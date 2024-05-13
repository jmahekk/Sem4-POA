
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

data segment
seg1 db 1h,2h,3h
ends

extra segment
seg2 db ?
ends
   

start:
mov ax,data
mov ds,ax
mov ax,extra
mov es,ax
lea si,seg1
lea di,seg2
mov cx,03h
x: mov ah,ds:[si]
mov es:[di],ah

inc si
inc di
dec cx
jnz x 
HLT
ends
end start

ret




