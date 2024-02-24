import math

def tabula(lim_inf, lim_sup, inc):
    print("---X---|---F(X)---")
    item = lim_inf
    while item <= lim_sup:
        print("   " + str(item) + "   |   " + str(f(item)))
        item += inc
    print("---------------")
    
    
def f(x):
    return (-2.1 + (6.21 * x)) - (3.9 * (x ** 2)) + (0.667 * math.pow(x, 3))
    
lim_inf = float(input("Ingresa el limite inferior: "))    
lim_sup = float(input("Ingresa el limite superior: "))    
inc = float(input("Ingresa el incremento: "))

tabula(lim_inf, lim_sup, inc)
