# name="Baylor"
# count=len(name)
# print(name)
# print(count)
def length_finder (string):
  return len(string)

print(length_finder ("Josie"))

# name="lovely"
# first_two=name[0]+name[1]
# last_two=name[-2]+name[-1]
# print(first_two+last_two)

def string_shortener(string_to_shorten):
  first_two_chars = string_to_shorten[0:2]
  last_two_chars = string_to_shorten[-2:]
  return f"{first_two_chars}{last_two_chars}"

print(string_shortener ("howdy there friend"))


# def change_char(name):
#   char = name[0]
#   name = name.replace(char, '$')
#   name = char + name[1:]

#   return name

# print(change_char('babbling bumbling band of baboons'))

def replace_char(string):
  