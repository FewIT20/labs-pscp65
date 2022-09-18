"""IG: few.pz"""
def check_time_ms(text, status):
    """Main Function"""
    if text.count('out.') >= 1 or text.count('fail') >= 1:
        return 1
    else:
        if status == 2:
            return text[text.find("time") + 4:text.find("ms")]
        else:
            return 0

def main():
    """Main Function"""
    a_val, b_val, c_val, d_val, e_val, f_val, j_val, ip_address = input(), input(), \
input(), input(), input(), input(), input(), ''

    #ไม่ได้เอาไปใช้งั้นตกแต่งให้สวยงาม
    a_val.count("真そばに　いて欲しい")
    b_val.count("あなたと一緒じゃなきゃだめなんだ")

    if c_val.count("[") <= 0:
        ip_address = c_val[c_val.find("Pinging ") + 8:c_val.find(" with")]
    else:
        ip_address = c_val[c_val.find("[") + 1:c_val.find("]")]
    mil_time = check_time_ms(d_val, 1) + check_time_ms(e_val, 1) +\
         check_time_ms(f_val, 1) + check_time_ms(j_val, 1)
    print('Ping statistics for %s:' %(ip_address))
    print('    Packets: Sent = 4, Received = %d, Lost = %d (%s loss),' \
%(abs(int(mil_time) - 4), int(mil_time), str(int(mil_time) * 25) + "%"))
    if mil_time < 4:
        time1, time2, time3, time4 = str(check_time_ms(d_val, 2)), \
str(check_time_ms(e_val, 2)), str(check_time_ms(f_val, 2)), str(check_time_ms(j_val, 2))
        print('Approximate round trip times in milli-seconds:')
        if str(time1).count("<") >= 1 or str(time2).count("<") or str(time3).count("<")\
 or str(time4).count("<"):
            print('    Minimum = 0ms, Maximum = 0ms, Average = 0ms')
        else:
            maximum = max(int(-1 if time1[1:] == "" else time1[1:]), int(-1 if time2[1:] == "" \
else time2[1:]), int(-1 if time3[1:] == "" else time3[1:]), int(-1 if time4[1:] == "" else \
time4[1:]))
            minimum = min(int(1000000 if time1[1:] == "" else time1[1:]), int(1000000 \
if time2[1:] == "" else time2[1:]), int(1000000 if time3[1:] == "" else time3[1:]), \
int(1000000 if time4[1:] == "" else time4[1:]))
            print('    Minimum = %dms, Maximum = %dms, Average = %dms' %(minimum, maximum,\
 (int(0 if time1[1:] == "" else time1[1:]) + int(0 if time2[1:] == "" \
else time2[1:]) + int(0 if time3[1:] == "" else time3[1:]) + int(0 if time4[1:] == "" \
else time4[1:])) / (abs(mil_time - 4))))
main()
