Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
import sys
file = open("Mips.txt","r+")
lines = []
mem = 492
def signedint(val, bit):
    if (val & (1 << (bit - 1))) != 0:
        val = val - (1 << bit)        
    return val
for line in file:
        if line.strip():
            lines.append(line) 
            mem = mem + 4
            print(line)
            
            opcode = int(line[0:6],2)
            rs = int(line[6:11],2)
            rt = int(line[11:16],2)
            rd = int(line[16:21],2)
            SA = int(line[21:26],2)
            func =int(line[26:32],2)
            imm  = line[16:32]
            offset = line[16:32]
            
        if opcode == 0  and SA == 0 and func == 32:
            print(mem,"\tADD\t"  "R%d "%rd, "R%d  "%rs,  "R%d "%rt)
            
        if opcode == 0  and SA == 0 and func == 33:
            print(mem,"\tADDU\t"   "R%d "%rd, "R%d  "%rs,  "R%d "%rt)
            
        if opcode == 0  and SA == 0 and func == 34:
            print(mem,"\tSUB\t"  "R%d "%rd, "R%d  "%rs,  "R%d "%rt)
            
        if opcode == 0  and SA == 0 and func == 35:
            print(mem,"\tSUBU\t"  "R%d "%rd, "R%d  "%rs,  "R%d "%rt)
            
        if opcode == 0  and rd == 0 and SA == 0 and func == 24:
            print(mem,"\tMUL\t"   "R%d "%rs, "R%d "%rt)
            
        if opcode == 0  and rd == 0 and SA == 0 and func == 25:
            print(mem,"\tMULU\t"   "R%d "%rs, "R%d "%rt)
            
        if opcode == 0 and rd == 0 and SA == 0 and func == 26:
            print(mem,"\tDIV\t" "R%d "%rs, "R%d "%rt)
            
        if opcode == 0 and rd == 0 and SA == 0 and func == 27:
            print(mem,"\tDIVU\t" "R%d "%rs, "R%d "%rt)
            
        if opcode == 8:
            a = signedint(int(imm,2), len(imm))
            print (mem,"\tADDI\t" "R%d "%rt, "R%d  "%rs, "#",a)
            
        if opcode == 9:
            
            print (mem,"\tADDIU\t" "R%d "%rt, "R%d  "%rs, "#",a)
            
        if opcode == 0 and SA == 0 and func == 42:
            print(mem,"\tSLT\t" "R%d "%rd, "R%d "%rs,"R%d "%rt )
            
        if opcode == 10:
            a = signedint(int(imm,2), len(imm))
            print (mem,"\tSLTI\t" "R%d "%rt, "R%d  "%rs, "#",a)
            
        if opcode == 0 and SA == 0 and func == 36:
            print(mem,"\tAND\t"  "R%d "%rd, "R%d  "%rs,  "R%d "%rt)
            
        if opcode == 0 and SA == 0 and func == 37:
            print(mem,"\tOR\t"  "R%d "%rd, "R%d  "%rs,  "R%d "%rt)
            
        if opcode == 0 and SA == 0 and func == 39:
            print(mem,"\tNOR\t"  "R%d "%rd, "R%d  "%rs,  "R%d "%rt)
            
        if opcode == 0 and SA == 0 and func == 40:
            print(mem,"\tXOR\t"  "R%d "%rd, "R%d  "%rs,  "R%d "%rt)
            
        if opcode == 35:
            b = "R%d  "%rs
            c = int(offset,2)
            print (mem,"\tLW\t" "R%d  "%rt, c,"("+ b +")" )
            
        if opcode == 43:
            b = "R%d  "%rs
            c = int(offset,2)
            print (mem,"\tSW\t" "R%d  "%rt, c,"("+ b +")" )
            
        if opcode == 1 and func == 1:
            print (mem,"\tSLL\t" "R%d "%rd,"R%d  "%rt, SA )
            
        if opcode == 0 and func == 2:
            print (mem,"\tSLL\t" "R%d "%rd,"R%d  "%rt, SA )   
            
        if opcode == 0 and func == 3:
            print (mem,"\tSLL\t" "R%d "%rd,"R%d  "%rt, SA )
        if opcode == 2:
            e = 4 * int(line[6:32],2)
            print (mem,"\tJ\t", "#",+e )
        if opcode == 0 and rd == 0 and rt == 0 and SA == 0 and func == 8:
            print(mem,"\tJR\t" "R%d "%rs)
            
        if opcode == 4:
            h = 4 * int(imm,2)
            print (mem,"\tBEQ\t" "R%d "%rs,"R%d  "%rt, "#",h )
            
        if opcode == 5:
            h = 4 * int(imm,2)
            print (mem,"\tBNE\t" "R%d "%rs,"R%d  "%rt, "#",h )
            
        if opcode == 1 and rt == 1:
            h = 4 * int(imm,2)
            print(mem,"\tBGEZ\t" "R%d "%rs,"R%d  "%rt, "#",h)
        
        if opcode == 1 and rt == 0:
            h = 4 * int(imm,2)
            print(mem,"\tBLTZ\t" "R%d "%rs,"R%d  "%rt, "#",h)
        
        if opcode == 6 and rt == 0:
            h = 4 * int(imm,2)
            print(mem,"\tBLEZ\t" "R%d "%rs,"R%d  "%rt, "#",h)
         
        if opcode == 7 and rt == 0:
            h = 4 * int(imm,2)
            print(mem,"\tBZTZ\t" "R%d "%rs,"R%d  "%rt, "#",h)
            
        if opcode == 0 and func == 13:
            print(mem,"\tBREAK")
            
        if opcode == 0  and func == 0:
            print(mem,"\tNOP")
        if int(line[0:32],2) == 0:
            print(mem,0)
        if int(line[0:32],2) == 4294967295:
            a = signedint(int(line[0:32],2), len(line[0:32]))
            print(mem, a)
        if int(line[0:32],2)==1:
            print(mem,int(line[0:32],2))
            
        if int(line[0:32],2) == 2147483648:
            a = signedint(int(line[0:32],2), len(line[0:32]))
            print(mem, a)
            
        if int(line[0:32],2) == 1431655765:
            a = signedint(int(line[0:32],2), len(line[0:32]))
            print(mem, a) 
        for i in range(len(line)):
            if (i%2)==0:
                b=line[i]
