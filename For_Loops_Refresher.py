list_a = ["Gorillaz", "Guitar", "Python"]

for element in list_a:
    print(element)

list_b = [20, 97, 22]
total = 0
for element in list_b:
    total += element
print(total)

list_c = range(1, 5)
total = 0
for e in list_c:
    total += e
print(total)

c = list(range(1, 5))
print(c)

sum = 0
for i in range(1, 11):
    sum += i
print(sum)

print(list(range(1, 26)))

sum = 0
for i in range(1, 25):
    sum += i
print(sum)

print(list(range(1, 8)))

total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total3 += i
print(total3)

total_exercise = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total_exercise +=i
print(total_exercise)
