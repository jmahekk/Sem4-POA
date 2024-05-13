
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt
;MAHEK JOSHI  C081  60004220108

DATA SEGMENT
    ARR DB 5,3,7,1,9,2,6,8,4
    LEN DW $-ARR
    MIN DB ?
    MAX DB ?
    DATA ENDS

CODE SEGMENT
    ASSUME DS:DATA CS:CODE
    
    START:
    MOV AX,DATA
    MOV DS,AX
    
    LEA SI,ARR
    MOV AL,ARR[SI]
    MOV MIN,AL
    MOV MAX,AL 
    
    MOV CX, LEN
    REPEAT:
    MOV AL,ARR[SI]
    CMP MIN,AL
    JL CHECKMAX
    
    MOV MIN,AL
    CHECKMAX:
    CMP MAX,AL
    JG DONE
    
    MOV MAX,AL
    DONE:
    INC SI
    LOOP REPEAT
    
    MOV AH,4CH
    INT 21H
    CODE ENDS
END START

