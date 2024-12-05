import sys

input = sys.stdin.readline

Q = int(input())

table_name = {}   # name -> value
table_value = {}  # value -> name
values_list = []  # Sorted list of values

queries = [input().strip().split() for _ in range(Q)]

for query in queries:
    if query[0] == 'init':
        table_name.clear()
        table_value.clear()
        values_list.clear()
    elif query[0] == 'insert':
        name = query[1]
        value = int(query[2])
        if name in table_name or value in table_value:
            print("0")
        else:
            # Insert value into the sorted list without using bisect
            index = 0
            while index < len(values_list) and values_list[index] < value:
                index += 1
            values_list.insert(index, value)
            table_name[name] = value
            table_value[value] = name
            print("1")
    elif query[0] == 'delete':
        name = query[1]
        if name in table_name:
            value = table_name[name]
            # Find the index of the value without using bisect
            index = 0
            while index < len(values_list) and values_list[index] != value:
                index += 1
            if index < len(values_list):
                values_list.pop(index)
            del table_name[name]
            del table_value[value]
            print(value)
        else:
            print("0")
    elif query[0] == 'rank':
        k = int(query[1])
        if len(values_list) < k:
            print("None")
        else:
            value = values_list[k - 1]
            name = table_value[value]
            print(name)
    elif query[0] == 'sum':
        k = int(query[1])
        # Calculate the sum of values less than or equal to k without using bisect
        total_sum = 0
        for value in values_list:
            if value <= k:
                total_sum += value
            else:
                break
        print(total_sum)
