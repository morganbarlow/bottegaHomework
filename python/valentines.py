list_of_dictionaries = [{1: "a", 2: "b"}, {2: "c", 3: "d"}, {3: "e", 4: "f"}]

combine_dictionary = {}

for dictionary in list_of_dictionaries:
    for key in dictionary.keys():
        if key in combine_dictionary:
            if isinstance(combine_dictionary[key], list):
                combine_dictionary[key].append(dictionary[key])
            else:
                combine_dictionary[key] = [combine_dictionary[key]]
            combine_dictionary[key].append(dictionary[key])
        else:
            combine_dictionary[key] = dictionary[key]

print(combine_dictionary)
