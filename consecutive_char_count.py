n='aaabbccccdd'
c=1
i=0
s=''
while i<=len(n)-1:
    if i==len(n)-1:
        s+=(n[i]+str(c))
        break
    elif n[i]==n[i+1]:
        c+=1
        i+=1
    else:
        s+=(n[i]+str(c))
        c=1
        i+=1
print(s)
