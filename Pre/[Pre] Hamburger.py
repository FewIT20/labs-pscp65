"""Hamburger"""
 
def main():
    """Main function"""
    value_left = int(input())
    value_right = int(input())
 
    left_hamburger = "|"*value_left
    right_hamburger = "|"*value_right
 
    meat = "*"*(value_left*2 + value_right*2)
    print(left_hamburger + meat + right_hamburger)
 
 
main()
