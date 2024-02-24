def newtonRaphson(xi, err, counter):
    fxi = f(xi)
    fdxi = fd(xi)
    
    print("X"+str(counter)+": " +  str(xi))
    print("f(x"+str(counter)+"): " +  str(fxi))
    print("-----Fin de Iteracion: "+str(counter + 1)+" ------------")
    
    if abs(fxi) < err:
        return
    
    xm = xi - (fxi / fdxi)
    
    counter += 1
    newtonRaphson(xm, err, counter)
    
    
    
def f(x):
    return 0.667 * (x ** 3) - 3.9 * (x ** 2) + 6.21 * x - 2.1

def fd(x):
    return 2.001 * (x ** 2) - 7.8 * x + 6.21
    
xi = float(input("Ingresa el valor inicial: "))   
err = float(input("Ingresa el error aproximado: "))
print("---------------")

newtonRaphson(xi, err, 0)
