inp = [int(i) for i in input("Input a sorted array:").split(" ")]

ans_list = []


def divide(start, arr):
    if not arr:
        return
    mid = int(len(arr)/2)
    if arr[mid] == start+mid:
        ans_list.append(arr[mid])
        divide(start, arr[: mid])
        divide(mid+start+1, arr[mid+1:])
    elif arr[mid] < start+mid:
        divide(mid+start+1, arr[mid+1:])
    elif arr[mid] > start+mid:
        divide(start, arr[: mid])


divide(1, inp)
print(ans_list)
