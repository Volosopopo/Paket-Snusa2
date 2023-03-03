a=int(input())
q=a%10
#4
p=a/10
d=p%10
#3
p=p/10
h=p%10
#2
p=p/10
#1
s1=q+d
s2=h+p
if s1>s2:
    print("Summa pervih 2 bol'she 2 poslendih")
else:
    print("Summa pervih 2 ne bol'she 2 poslendih")
s=s2+s1
k3=s%3
if k3==0:
    print("Summa kratna 3")
else:
    print("Summa ne kratna 3")
pr=h+q+d+p
k4=pr%4
if k4==0:
    print ("Proiz kratno 4")
else:
    print ("Proiz ne kranto 4")
ka=a%pr
if ka==0:
    print ("Chislo kratno proiz")
else:
    print ("Chislo ne kratno proiz")