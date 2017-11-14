import sympy as sp
from sympy import *

x = sp.Symbol('x')
x1 = sp.Symbol('x1')
x11 = sp.Symbol('x11')
x12 = sp.Symbol('x12')
x13 = sp.Symbol('x13')
x2 = sp.Symbol('x2')
x21 = sp.Symbol('x21')
x22 = sp.Symbol('x22')
x23 = sp.Symbol('x23')
x3 = sp.Symbol('x3')
x31 = sp.Symbol('x31')
x32 = sp.Symbol('x32')
x33 = sp.Symbol('x33')
x4 = sp.Symbol('x4')
x41 = sp.Symbol('x41')
x42 = sp.Symbol('x42')
x43 = sp.Symbol('x43')
x5 = sp.Symbol('x5')
x51 = sp.Symbol('x51')
x52 = sp.Symbol('x52')
x53 = sp.Symbol('x53')
w_m = sp.Symbol('w_m')
w_m1 = sp.Symbol('w_m1')
w_m2 = sp.Symbol('w_m2')
w_m3 = sp.Symbol('w_m3')
n_g_value = sp.Symbol('n_g')
n_a_value = sp.Symbol('n_a')

x1 = Matrix([[x11],[x12],[x13]])
x2 = Matrix([[x21],[x22],[x23]])
x3 = Matrix([[x31],[x32],[x33]])
x4 = Matrix([[x41],[x42],[x43]])
x5 = Matrix([[x51],[x52],[x53]])
w_m = Matrix([[w_m1],[w_m2],[w_m3]])
n_g = Matrix([[n_g_value], [n_g_value], [n_g_value]])
n_a = Matrix([[n_a_value], [n_a_value], [n_a_value]])
x = Matrix([[x11],[x12],[x13],[x21],[x22],[x23],[x31],[x32],[x33],[x41],[x42],[x43],[x51],[x52],[x53]])

G = Matrix([[cos(x22),0,-cos(x21)*sin(x22)],
            [0,1,sin(x21)],
            [sin(x21),0,cos(x21)*cos(x22)]]
            )



x_diff = Matrix([[x31],[x32],[x33]])

a = G**(-1)*(w_m-x4-n_g)

# print(x3.jacobian(x))
c = a.jacobian(x)

# c = c.subs({x21:0,x22:0,x23:0,x41:1.2,x42:1.3,x43:1.4})

print(c)
