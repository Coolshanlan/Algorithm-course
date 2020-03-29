input_list = [int(i) for i in input('input').split(' ')]
history_min = input_list[0]
now_min = input_list[0]
now_max = input_list[0]
history_max = input_list[0]
for j in range(2, len(input_list)):
    value = input_list[j]
    if value < now_min:
        now_min = value
        now_max = value
    elif value > now_max:
        now_max = value
    if now_max - now_min > history_max-history_min:
        history_max = now_max
        history_min = now_min
if now_max - now_min > history_max-history_min:
    print(now_min, now_max)
else:
    print(history_min, history_max)
