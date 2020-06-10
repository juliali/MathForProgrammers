rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def is_valid(s):
    weight = 0
    w_count = 0

    for i in range(len(s) - 1, -1, -1):
        n_weight = rom_val[s[i]]

        if n_weight > weight:
            w_count = 1
        elif n_weight == weight:
            w_count += 1
        else: # n_weight < weight
            if weight / n_weight > 10:
                print("Invalid char:", s[i])
                return False
            else:
                w_count = 1

        if w_count > 3 and n_weight < 1000:
            print("Invalid char:", s[i])
            return False
        else:
            weight = n_weight

    return True


def roman_to_int(s):
    if not is_valid(s):
        print("ERROR: The input {0} is invalid!".format(s))
        return

    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]

    print("The integer value of {0} is {1}.".format(s, int_val))
    return int_val

roman_to_int('IIIM')
roman_to_int('VVVV')
roman_to_int('LVII')
roman_to_int('LXII')
roman_to_int('CDXLIII')
roman_to_int('DCDXCVII')
roman_to_int('MIII')
roman_to_int('MMMCMLXXXVI')
roman_to_int('MMMMMMMMMMMM')

