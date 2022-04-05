# exercicio 1

def PA(a1,r,x):
    l=[a1]
    k=a1
    while k+r<=x:
        k+=r
        l.append(k)
    print(l)
def PG(a1,r,x):
    l=[a1]
    k=a1
    while k*r<=x:
        k*=r
        l.append(k)
    print(l)

def progressão():
    a1=int(input("Valor inicial: "))
    r=int(input("Razão: "))
    x=int(input("Valor limite: "))
    if(r%2==0):
        PA(a1,r,x)
    else:
        PG(a1,r,x)

progressão()

#exercicio 2

def contar1():
    x=int(input("Diga o número: "))
    count=0
    while x!=0:
        resto=x%2
        x//=2
        if (resto==1):
            count+=1
    print(count)

contar1()

#exercicio 3

count=0
i=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0
while i*1+j*2+k*5+l*10+m*20+n*50+o*100+p*200<=200:
    while i*1+j*2+k*5+l*10+m*20+n*50+o*100+p*200<=200:
        while i*1+j*2+k*5+l*10+m*20+n*50+o*100+p*200<=200:
            while i*1+j*2+k*5+l*10+m*20+n*50+o*100+p*200<=200:
                while i*1+j*2+k*5+l*10+m*20+n*50+o*100+p*200<=200:                                        
                    while i*1+j*2+k*5+l*10+m*20+n*50+o*100+p*200<=200:                                                
                        while i*1+j*2+k*5+l*10+m*20+n*50+o*100+p*200<=200:
                            while i*1+j*2+k*5+l*10+m*20+n*50+o*100+p*200<=200:
                                if(i*1+j*2+k*5+l*10+m*20+n*50+o*100+p*200==200):
                                    count+=1
                                i+=1
                            j+=1
                            i=0
                        k+=1
                        j=0
                    l+=1
                    k=0
                m+=1
                l=0
            n+=1
            m=0
        o+=1
        n=0
    p+=1
    o=0
print('De',count,'maneiras diferentes')

#exercicio 4

x=0
for i in range(1000):
    x+=(i+1)**(i+1)
print(x)
print('Os últimos dez dígitos são',x%10000000000)