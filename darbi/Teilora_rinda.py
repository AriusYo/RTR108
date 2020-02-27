import math
x = float(input("Lietotāj, ievadiet x vērtību:"))
y = math.cos(x*x)
print("y=cos(%g)=%1.3f" %(x*x,y))

a = pow(-1,0)*pow(x,0)/(1.)
S = a
print("\tx\ta\tS")
print("\t{}\t{}\t{}".format(x,a,S))

for k in range(1, 501):
    a = a*(-1)*pow(x,4)/(((2*k)-1)*(2*k))
    S = S + a
    if(k == 499):
        a499 = a
    if(k == 500):
        a500 = a

print("%.2f\t%.2f\t%.2f\t%.2f" %(k,x,a,S))
print("priekšpēdējā saskaitāmā vērtība: %.5f" %a499)
print("pēdējā saskaitāmā vērtība: %.5f" %a500)
print("\n\t            4")
print("\t          -x^")
print("\tR =  ----------------")
print("\t      (2*k-1)*(2*k)")
print("\n");

print("\n\t\t  500")
print("\t\t______")
print("\t\t\\               k  4*k")
print("\t\t \\          (-1)^*x^")
print("\ty(x)=\t  |     --------------   = cos(x*x)")
print("\t\t /           (2*k)!")
print("\t\t/      ")
print("\t\t------")
print("\t\t  k=0")



