"""IG: few.pz"""
 
 
def x_func(value):
    """Functions fog"""
    return 2*value
 
 
def g_func(value):
    """Functions gof"""
    return (value/2) + 1
 
 
def main():
    """Main function"""
    value = int(input())
    print("%.2f" % (x_func(g_func(value))))
    print("%.2f" % (g_func(x_func(value))))
 
 
main()
