def quadratic(a, b, c):
    x1 = (-b+(b**2 - 4*a*c)**.5) / (2 * a)
    x2 = (-b-(b**2 - 4*a*c)**.5) / (2 * a)
    print(x1)
    print(x2)


quadratic(2, 3, 4)
""" 
(-0.7499999999999999+1.1989578808281798j)
(-0.7500000000000001-1.1989578808281798j)

 """