import timeit

list1 = []
for i in range(200000):
    list1.append(i)

def print_time(n):
    start_time = timeit.timeit()
    print("printing "+ str(n)+ " took ", end="")
    end_time = timeit.timeit()
    time_taken = float(end_time - start_time)
    time_taken = float("{0:.5f}".format(time_taken))
    print(str(time_taken) + " long")

print_time(1)
print_time(10)
print_time(100)
print_time(1000)
print_time(10000)
print_time(100000)
print_time(150000)
print_time(199999)