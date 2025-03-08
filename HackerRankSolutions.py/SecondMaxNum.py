nums = list(map(int, input( ).split()))
sorted_list = list(set(nums))
sorted_list.sort(reverse=True)

if len(sorted_list) >= 3:
    print(sorted_list[2])
else:
    print(sorted_list[0])
