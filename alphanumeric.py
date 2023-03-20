n='121a222bb44ccd454d111ds55!6665x8'
c=1
i=0
s=[]
while i<=len(n)-1:
    if i==len(n)-1 and n[i].isdigit():
        s.append(str(n[i-c+1:i+1]))
        break
    #For similar consective numbers only add below 'and n[i]==n[i+1]'
    elif n[i].isdigit()  and n[i+1].isdigit() :
        c+=1
        i+=1
    else:
        if n[i].isdigit():
            s.append(str(n[i-c+1:i+1]))
        c=1
        i+=1
print(s)
