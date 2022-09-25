"""IG: few.pz"""
def output_value(time1, time2, time3, time4, value):
    """Output value"""
    if time1[1:] == "":
        value1 = value
    else:
        value1 = time1[1:]
    if time2[1:] == "":
        value2 = value
    else:
        value2 = time2[1:]
    if time3[1:] == "":
        value3 = value
    else:
        value3 = time3[1:]
    if time4[1:] == "":
        value4 = value
    else:
        value4 = time4[1:]
    return int(value1), int(value2), int(value3), int(value4)

def get_time_millisecond(text, status):
    """Check time millisecond"""
    if text.count('out.') >= 1 or text.count('fail') >= 1:
        return 1
    else:
        if status == 2:
            return text[text.find("time") + 4:text.find("ms")]
        else:
            return 0

def main():
    """Main Function"""
    input()
    input()
    # ^^ input() unused less than 2 times
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    line5 = input()
    ip_address = ""

    if line1.count("[") <= 0:
        ip_address = line1[line1.find("Pinging ") + 8 : line1.find(" with")]
    else:
        ip_address = line1[line1.find("[") + 1 : line1.find("]")]
    millisecond = get_time_millisecond(line2, 1) + get_time_millisecond(line3, 1) \
        + get_time_millisecond(line4, 1) + get_time_millisecond(line5, 1)
    print('Ping statistics for %s:' %(ip_address))
    print('    Packets: Sent = 4, Received = %d, Lost = %d (%s loss),' % \
        (abs(int(millisecond) - 4), int(millisecond), str(int(millisecond) * 25) + "%"))
    if millisecond < 4:
        time3 = str(get_time_millisecond(line4, 2))
        time4 = str(get_time_millisecond(line5, 2))
        print('Approximate round trip times in milli-seconds:')
        if str(get_time_millisecond(line2, 2)).count("<") >= 1 or \
            str(get_time_millisecond(line3, 2)).count("<") or time3.count("<") or time4.count("<"):
            print('    Minimum = 0ms, Maximum = 0ms, Average = 0ms')
        else:
            value1, value2, value3, value4 = output_value(str(get_time_millisecond(line2, 2)), \
                str(get_time_millisecond(line3, 2)), time3, time4, -1)
            maximum = max(value1, value2, value3, value4)
            value1, value2, value3, value4 = output_value(str(get_time_millisecond(line2, 2)), \
                str(get_time_millisecond(line3, 2)), time3, time4, 1000000)
            minimum = min(value1, value2, value3, value4)
            value1, value2, value3, value4 = output_value(str(get_time_millisecond(line2, 2)), \
                str(get_time_millisecond(line3, 2)), time3, time4, 0)
            print('    Minimum = %dms, Maximum = %dms, Average = %dms' %\
                (minimum, maximum, int((int(value1) + int(value2) + int(value3) + int(value4)) \
                    / (abs(millisecond - 4)))))
main()
