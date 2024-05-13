org 100h
;MOV AX,[1000h] 
;MOV BX,[1002h]
;MOV CL,00h
;ADD AX,BX
;MOV [1004h],AX
;JNC jump
;INC CL
;jump:
;MOV [1006h],CL
;HLT
;ret
MOV AX,[1000h]
MOV BX,[1002h]
MOV CL,00h   
CLC
SBB AX,BX
MOV [1004h],AX
JNC jump
INC CL
jump:
MOV [1006h],CL
HLT 
ret



