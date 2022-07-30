total = 0
for i in range(1, 5):
    total += i
print(total)

total2 = 0
j = 1
while j < 5:
    total2 += j
    j += 1
print("While loop:",total2)

given_list = [5, 4, 4, 3, 1]

total3 = 0
i = 0
while i < len(given_list) and given_list[i] > 0:
    total3 += given_list[i]
    i += 1
print(total3)

given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total4 = 0
for e in given_list2:
    if e <= 0:
        break
    total4 += e
print(total4)

given_list3 = [5, 4, 4, 3, 1, -2, -3, -5]
total_positive = 0
total_negative = 0
for element in given_list3:
    if element <= 0:
        total_negative += element
    else:
        total_positive += element
print("total positive:",total_positive)
print("total negative:",total_negative)

total5 = 0
i = 0
while True:
    total5 += given_list2[i]
    i += 1
    if given_list2[i] <= 0:
        break
print(total5)

given_list4 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total6 = 0
i = 0
while True:
    if given_list4[i] > 0:
        total6 += i
    if given_list4[i] <= 0:
        break
print("hjnikopsjg", total6)