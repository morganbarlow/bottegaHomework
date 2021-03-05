from functools import reduce
quiz_grades = [98, 94, 96, 97, 99, 97]
print(reduce(lambda total, element: total+element, quiz_grades))


user_string = input('String:').split(',')
sorted_string = sorted(user_string)
print(sorted_string)

def char_counter(string_to_count):
  char_counts = {}

  for char in string_to_count:
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1
      
  return char_counts

print(char_counter("how are you today?"))

# I couldn't figure out the last one
# Went over it in class


""""
Alex's way

#1 the first way
from functools import reduce
def list_sum(list_to_sum):
  return reduce(lambda total,next_element: total + next_element,list_to_sum)
my_list=[98, 94, 96, 97, 99, 97]
print(list_sum(my_list))

#1 a different way
def list_sum(list_to_sum):
  return sum(list_to_sum)
my_list=[98, 94, 96, 97, 99, 97]
print(sum(my_list))


def string_sorter(string_to_sort):
  string_to_list = string_to_sort.split(",")
  string_to_list.sort()
  return ",".join(string_to_list)

print(string_sorter("orange,banana,apple,lemon"))


def char_counter(string_to_count):
  char_counts = {}

  for char in string_to_count:
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1
      
  return char_counts

print(char_counter("how are you today?"))
"""