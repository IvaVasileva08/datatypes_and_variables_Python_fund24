start_index = int(input())
second_index = int(input())
for index in range(start_index, second_index + 1):
    if index == second_index:
        print(chr(index))
    else:
        print(chr(index), end = " ")