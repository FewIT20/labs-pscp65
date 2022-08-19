"""IG: few.pz"""
import math
 
 
def kareen_five():
    """Kareen five functions"""
    head = math.log(4234, 5) + math.log(8191, 2) + 71 * math.log(156154, 10)
    body = math.log(777, 7) - math.log(888, 8) - math.log(999, 9)
    print(head/body)
 
 
def kareen_four():
    """Kareen four functions"""
    head = math.log(1234**4, 10)
    print(head)
 
 
def kareen_there():
    """Kareen there functions"""
    head = 15 + 25
    body = math.sqrt((25-12)**2 + (12-15)**2)
 
    print(head/body)
 
 
def kareen_two():
    """Kareen two functions"""
    head = math.factorial(16) * math.factorial(4)
    body = math.factorial(8)
 
    total = head/body
    print(total)
 
 
def kareen_one():
    """Kareen one functions"""
    head = math.sin(math.radians(90)) + math.sin(math.radians(60))**2
    body = math.cos(math.radians(245**2)) + math.cos(math.radians(45 + 135))
 
    total = head/body
    print(total)
 
 
def main():
    """Main functions"""
    kareen_one()
    kareen_two()
    kareen_there()
    kareen_four()
    kareen_five()
 
 
main()