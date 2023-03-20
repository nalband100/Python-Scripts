n=input()
#input : apple
l=[]
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        l.append(n[i:j])
print(l)
