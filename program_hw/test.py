from time import clock

num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")


def decompose(number):
    decompose_list = []       # 列表中存储三个元素，分别对应A B n，即三个分解元素
    length = len(number) // 2
    decompose_fator_1 = int(number[:-length])
    decompose_fator_2 = int(number[-length:])

    decompose_list.append(decompose_fator_1)
    decompose_list.append(decompose_fator_2)
    decompose_list.append(length)

    return decompose_list


def karatsuba(number1, number2):
    decompose_number1_list = decompose(number1)     # 得到两个数字的分解元素
    decompose_number2_list = decompose(number2)

    # A*C
    multiplication_item_1 = decompose_number1_list[0] * \
        decompose_number2_list[0]
    # B*D
    multiplication_item_3 = decompose_number1_list[1] * \
        decompose_number2_list[1]
    multiplication_item_2 = (decompose_number1_list[0] + decompose_number1_list[1]) * \
                            (decompose_number2_list[0] + decompose_number2_list[1]) - \
                            (multiplication_item_1 +
                             multiplication_item_3)     # AD + BC

    final_result = multiplication_item_1 * 10 ** (decompose_number1_list[2] + decompose_number2_list[2]) + \
        multiplication_item_2 * \
        10 ** (decompose_number1_list[2]) + multiplication_item_3

    return final_result


# Karatsuba 算法并测试用时
t1 = clock()
result = karatsuba(num1, num2)
t2 = clock()
print("{}        use time: {:.8f}".format(result, t2-t1))

# 普通乘法并测试用时
t3 = clock()
result = int(num1) * int(num2)
t4 = clock()
print("{}        use time: {:.8f}".format(result, t4-t3))
