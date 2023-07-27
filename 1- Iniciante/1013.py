a = int(input())
b = int(input())
c = int(input())
bigger = a

if b >= a and b >= c:
  bigger = b
elif c >= a and c >= b:
  bigger = c

print("{} eh o maior".format(bigger))