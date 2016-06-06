# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file not exists just return 0

def counts_a_letters(filename):
    try:
        f = open(filename)
        text = f.read()
        f.close()
        letter_a_num = 0
        for char in text:
            if char == 'a':
                letter_a_num += 1
        return letter_a_num
    except FileNotFoundError:
        return 0


print(counts_a_letters('haho.txt'))
print(counts_a_letters('text.txt'))
