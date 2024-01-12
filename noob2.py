# Program to calculate the sum of numbers until the user enter zero
total = 0

num = int(input("enter a number :"))

while num != 0:
  total += num
  num = int(input("enter a number :"))

print("Total of numbers :", total)