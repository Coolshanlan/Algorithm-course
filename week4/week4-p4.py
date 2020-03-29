import pretty_errors


def merge(l1, l2):
    #global invers
    index_l = 0
    index_r = 0
    left_max = len(l1)
    right_max = len(l2)
    merge_list = []
    # Sort left list
    while not (index_l == left_max or index_r == right_max):
        if l1[index_l] > l2[index_r]:
            merge_list.append(l2[index_r])
            index_r += 1
        else:
            merge_list.append(l1[index_l])
            invers += index_r
            index_l += 1
    for i in range(index_l, left_max):
        merge_list.append(l1[i])
        invers += index_r
    for i in range(index_r, right_max):
        merge_list.append(l2[i])
    return merge_list


def merge_sort(number_list):  # divide
    if len(number_list) <= 1:
        return number_list
    mid = len(number_list)/2
    mid = int(mid)
    l1 = merge_sort(number_list[:mid])
    l2 = merge_sort(number_list[mid:])
    return merge(l1, l2)


global invers
invers = 0
if __name__ == "__main__":
    input_list = input("input numbers(ex 1 4 3):").split(' ')
    input_list = [int(d) for d in input_list]
    print(merge_sort(input_list), invers)
