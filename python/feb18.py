# - Build 2 python classes.
# - One class must inherit from the other.
# - At least one class must have a __init__ constructor function.
# - At least one class must have a __str__ function.
# - At least one class must have a __repr__ function.
# - Between your two classes, you must have at least 5 instance attributes, and 1 class attribute.
# - Between your two classes, you must have at least 3 instance methods (not including __init__, __str__, or __repr__)
# - One method must use polymorphism.

our_states={
  'Alabama',
  'Alaska',
  'Arizona',
  'Arkansas',
  'California',
  'Colorado',
  'Connecticut',
  'Delaware',
  'Florida',
  'Georgia',
  'Hawaii',
  'Idaho',
  'Illinois',
  'Indiana',
  'Iowa',
  'Kansas',
  'Kentucky',
  'Louisiana',
  'Maine',
  'Maryland',
  'Michigan',
  'Minnesota',
  'Mississippi',
  'Missouri',
  'Montana',
  'Nebraska',
  'Nevada',
  'New Hampshire',
  'New Jersey',
  'New Mexico',
  'New York',
  'North Carolina',
  'North Dakota',
  'Ohio',
  'Oklahoma',
  'Oregon',
  'Pennsylvania',
  'Rhode Island',
  'South Carolina',
  'South Dakota',
  'Tennessee',
  'Texas',
  'Utah',
  'Vermont',
  'Virginia',
  'Washington',
  'West Virginia',
  'Wisconsin',
  'Wyoming'
}

our_territories = {
  'American Samoa',
  'District of Columbia',
  'Guam',
  'Northern Marianas Islands',
  'Puerto Rico',
  'Virgin Islands',
}

class States:
  def __init__(self,states):
    self.states = states

  def state (states):
    for state in states:
      if states in our_states:
        return (f'Yes, {states} is in the United States.')
      else:
        return (f'No, {states} is not a state.')
    
# class Territories(States):
def territory (territories):
  for territory in territories:
    if territory in our_territories:
      return f'Yes, {territories} is a United States territory!' 

    
print(States('Idaho'))
print(States('Jess'))