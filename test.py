def find_first_tenevennumbers():
  count = 0
  for number in range(1,100):
    if (number % 2 == 0 and count < 10):
      print(number)
      count +=1

find_first_tenevennumbers()