"""
5
25 36 48 29 95
"""
n = int(input())
marks = list(map(int, input().split()))

even = 0
odd = 0
"""if (n % 2 == 0):
    n1 = n // 2
    n2 = n // 2
else:
    n1 = (n // 2)+1
    n2 = (n // 2)
"""
n1=0
n2=0

for i in range(0, n, 2):
    even = even + marks[i]
    n1=n1+1

for i in range(1, n, 2):
    odd = odd + marks[i]
    n2=n2+1

print(((even) / n1) - ((odd) / n2))