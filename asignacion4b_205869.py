def reglaFalsa(xi, xd, err, counter):
    fxi = f(xi)
    fxd = f(xd)
    
    if abs(fxi) < err or abs(fxd) < err:
        return
    
    xm = ((xi*fxd) - (xd * fxi)) / (fxd - fxi)
    fxm = f(xm)
    
    print("Xi: " +  str(xi))
    print("f(xi): " +  str(fxi))
    print("Xd: " +  str(xd))
    print("f(xd): " +  str(fxd))
    print("Xm: " +  str(xm))
    print("f(xm): " +  str(fxm))
    print("-----Fin de Iteracion: "+str(counter)+" ------------")
    
    if fxm < 0 and fxi < 0:
        xi = xm
        
    if fxm < 0 and fxd < 0:
        xd = xm
    
    if fxm > 0 and fxi > 0:
        xi = xm
        
    if fxm > 0 and fxd > 0:
        xd = xm
    
    counter += 1
    reglaFalsa(xi,xd, err, counter)
    
    
    
def f(x):
    return (1-(0.6 * x))/x
    
xi = float(input("Ingresa el valor inicial: "))    
xd = float(input("Ingresa el valor final: "))    
err = float(input("Ingresa el error aproximado: "))
print("---------------")

reglaFalsa(xi, xd, err, 1)
