import mpmath
from sympy import *
import numpy as np
from scipy.misc import derivative
import sympy as sp


def deriv(f,x):
    my_f1 = sp.diff(f,x)
    return lambdify(x, my_f1)


# Prints root of func(x)
# with error of EPSILON
def bisection(func,a, b,eps,func_or_derive):
    max_itr = -(np.log(eps / (b - a))) / np.log(2)
    iter = 0
    if (func_or_derive=='fun'):
        if (func(a) * func(b) >= 0):

            return
    else:
        if (func(a) * func(b) > 0):
            return
    c = a
    while ((b - a) >= eps):
        if (iter > max_itr):
            break
        iter+=1
        # Find middle point
        c = (a + b) / 2
        if (np.any(np.absolute(c) < eps)):
            c=0
        # Check if middle point is root
        if (func(c) == 0.0):
            break
        # Decide the side to repeat the steps
        if (func(c) * func(a) < 0):
            b = c
        else:
            a = c
    return c

'''
2
'''
def func_2(f, start_point , end_point, num_of_split):

    fx=f
    x1 = sp.symbols('x')
    f=lambdify(x1,f)
    length=(end_point-start_point)/num_of_split

    x=start_point
    while(x<end_point):
        if f(x)* f(x+length)<=0:
          c=bisection(f,x,x+length,10**-10,'fun')
          if (c!=None):
            print("The value of root is : ", "%.4f" % c)
        x=x+length

    '''
    derive check
    '''
    x=start_point
    fd = deriv(fx,x1)
    while(x<end_point):
        a=fd(x)
        b=fd(x + length)
        if (a * b)<= 0:
            c=bisection(fd, x, x + length, 10 ** (-10),'der')
            if (c!= None):
                if((f(c)==0)):
                    print("The value of root is : ", "%.4f" % c)
        x= x + length



x = sp.symbols('x')
f=x**4+x**3-3*x**2
func_2(f,-5,10,40)