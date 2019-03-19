def get_long_string(s):
    long_s = ''
    for i in range(15):
        long_s = long_s + s
    return long_s


def cyclicStringRecurs(sub_string, s):
    long_sub_string = get_long_string(sub_string)
    if s in long_sub_string:
        return len(sub_string)
    else:
        return cyclicStringRecurs(s[:len(sub_string) + 1], s)


def cyclicString(s):
    sub_string = s[0]
    return cyclicStringRecurs(sub_string, s)