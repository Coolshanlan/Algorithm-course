import pretty_errors


def karatsuba(num1, num2):
    if len(num1) <= 2 or len(num2) <= 2:
        return str(int(num1) * int(num2))
    num_len = max(len(num1), len(num2))
    num_len_2 = num_len/2
    x = num1[:num_len_2]
    y = num1[num_len_2+1:]
    w = num2[:num_len_2]
    z = num2[num_len_2+1:]
    xw = karatsuba(x, w)
    yz = karatsuba(y, z)
    plus_xy_wz = karatsuba(x+y, w+z)


print(2345)
