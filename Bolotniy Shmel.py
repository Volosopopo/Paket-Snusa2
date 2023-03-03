a=int(input())
q=a%10
#3
p=a/10
d=p%10
#2
p=p/10
#1
s=p+d+q
if 9<s<100:
    print("Summa dvuhznachnoe")
else:
    print("Summa ne dvuhznachnoe")
h=q*d*p
if 99<h<1000:
    print("Proiz trehznach")
else:
    print("Proiz ne trehznach")
if h<a:
    print("Chislo bol'she summi")
else:
    print("Chislo ne bol'she summi")
o=s%5
if o==0:
    print("Summa kratna 5")
else:
    print("Summa ne kratna 5")
f=a%s
if f==0:
    print("Chislo kratno summe")
else:
    print("Chislo ne kratno summe")