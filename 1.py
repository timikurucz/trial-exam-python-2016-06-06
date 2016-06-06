# Create a function that takes a list as a parameter,
# and returns a new list with all it's element value doubled.
# It should raise an error if the parameter is not a list

def doubled_elements (input):
    doubled_list = []
    try:
            if type(input) is list:
                for i in range(len(input)):
                    doubled_list += [input[i] * 2]
                return doubled_list
            else:
                raise TypeError
    except TypeError:
        return 'Oops, the given parameter is not a list!'



print(doubled_elements('helloo'))
print(doubled_elements(3))
print(doubled_elements({3:4, 5:6}))
print(doubled_elements([1, 2, 3, 4]))
