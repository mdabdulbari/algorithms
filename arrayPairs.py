n = int(input())
printer = []
array =[int(e) for e in input() if(e != " ")]
tmp = array
for i in range(len(array) - 1):
    if array[i] > array[i +1]:
        (array[i], array[i +1]) = (array[i +1], array[i])
max = array[len(array) -1]
array = tmp
for i in range(len(array)):
    for j in range (i, len(array) - i - 1):
        if (array[i] * array[j + 1] <= max):
            print(array[i] ,array[j + 1])           
            printer.append((array[i], array[j + 1]))
print(array)           
print(printer) 