def swap(n1, n2):
    temp = n1
    n1 = n2
    n2 = temp
    # return n2,n1
    return n1, n2


def merge(l1, l2):
    index_l = -1
    index_r = 0
    left_max = len(l1)
    right_max = len(l2)

    # Sort left list
    for pos in range(left_max):
        if index_l == -1:
            if l1[pos] > l2[index_r]:
                l1[pos], l2[index_r] = swap(l1[pos], l2[index_r])
                index_l = index_r
                index_r += 1
        else:
            if l2[index_l] > l2[index_r]:
                l1[pos], l2[index_r] = swap(l1[pos], l2[index_r])
                index_r += 1
            else:
                l1[pos], l2[index_l] = swap(l1[pos], l2[index_l])
                index_l += 1
                # when list is 3 2 5 3 78 32 6 2 234 6 34 354 56 and do not have below code then program will be error at the last merge
                if index_l == index_r:
                    index_l = 0
    index_l2 = 0
    index_r2 = index_r
    if index_l == -1:
        l1.extend(l2)
        return l1

    # append right list element into left list
    while index_l2 < index_r and index_r2 < right_max:
        if l2[index_l2] < l2[index_r2]:
            l1.append(l2[index_l2])
            index_l2 += 1
        else:
            l1.append(l2[index_r2])
            index_r2 += 1
    for i in range(index_r2, right_max):
        l1.append(l2[i])
    for i in range(index_l2, index_r):
        l1.append(l2[i])
    return l1


def merge_sort(number_list):  # divide
    if len(number_list) <= 1:
        return number_list
    mid = len(number_list)/2
    mid = int(mid)
    l1 = merge_sort(number_list[:mid])
    l2 = merge_sort(number_list[mid:])
    return merge(l1, l2)


if __name__ == "__main__":
    input_list = input("input numbers(ex 1 4 3):").split(' ')
    input_list = [int(d) for d in input_list]
    print(merge_sort(input_list))
