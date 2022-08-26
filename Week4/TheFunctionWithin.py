"""IG: few.pz"""
 
 
def fun_x(val_x):
    """ f(x) = 2x """
    return 2 * val_x
 
 
def gun_x(val_x):
    """ g(x) = 3x^4 - x^3 + 2x^2 + 10 """
    return (3*pow(val_x, 4)) - pow(val_x, 3) + (2*pow(val_x, 2)) + 10
 
 
def hun_x(val_x, val_y, val_z):
    """ h(x, y, z) = (z + x)^2 - xy + y^2 """
    return pow(val_z+val_x, 2) - (val_x*val_y) + pow(val_y, 2)
 
 
def iun_x(val_a, val_b, val_c, val_d):
    """ i(a, b, c, d) = (a^2 + b^2 - c^2) / (d^2 - 2ad + 2a) """
    num = pow(val_a, 2) + pow(val_b, 2) - pow(val_c, 2)
    den = pow(val_d, 2) - (2*val_a*val_d) + (2*val_a)
    return num / den
 
 
def main():
    """ Main function """
    val_a = float(input())
    val_b = float(input())
    val_c = float(input())
    val_d = float(input())
 
    print(fun_x(fun_x(val_a)))
    print(gun_x(fun_x(val_a-val_b)))
    print(hun_x(fun_x(val_a+val_b), fun_x(val_a+val_c), gun_x(fun_x(pow(val_d, 2)))))
    ret_a = hun_x(fun_x(val_a+val_b), fun_x(val_a-val_c),
                  gun_x(fun_x(pow(val_d, 2))))
    ret_b = gun_x(fun_x(val_a-val_b))
    ret_c = fun_x(fun_x(fun_x(fun_x(fun_x(val_c)))))
    print(iun_x(ret_a, ret_b, ret_c, pow(val_d, 8)))
 
 
main()
