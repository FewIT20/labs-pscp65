"""IG: few.pz"""
def print_here(x_val):
    """Get string of text in value"""
    if x_val == 1:
        return "In Deep Learning, a Convolutional Neural Network (CNN) is a class \
of Deep Neural Networks, most commonly applied to analyzing visual imagery."
    if x_val == 2:
        return '"Two things are infinite: the universe and human stupidity; \
and I\'m not sure about the universe". - Albert Einstein'
    if x_val == 3:
        return "Statistics is the discipline that concerns the collection, \
organization, displaying, analysis, interpretation and presentation of data."
    if x_val == 4:
        return 'The backslash (\\) is a typographical mark used mainly in computing \
and is the mirror image of the common slash (/). It is sometimes called "escape character".'
 
def main():
    """Main function"""
    x_val = int(input())
    print(print_here(x_val))
 
main()
