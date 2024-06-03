
n = int(input())
m = int(input())

sum_of_multiples = 0
for i in range(m, n, m):
    print(i)
    sum_of_multiples += i
    print(sum_of_multiples)

