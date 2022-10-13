"""IG: few.pz"""
def rotate_down(correct_text, lock_text):
    """Rotate down"""
    rodown = 0
    while lock_text != correct_text:
        if lock_text >= 25:
            lock_text = -1
        rodown += 1
        lock_text += 1
    return rodown
def rotate_up(correct_text, lock_text):
    """Rotate up"""
    roup = 0
    while lock_text != correct_text:
        if lock_text <= 0:
            lock_text = 26
        roup += 1
        lock_text -= 1
    return roup
def main(correct, lock):
    """Safe"""
    count = 0
    for i in range(len(correct)):
        correct_text = ord(correct[i])-65
        lock_text = ord(lock[i])-65
        if correct_text != lock_text:
            rodown = rotate_down(correct_text, lock_text)
            roup = rotate_up(correct_text, lock_text)
            if roup <= rodown:
                count += roup
            elif rodown < roup:
                count += rodown
    print(count)
main(input().upper(), input().upper())
