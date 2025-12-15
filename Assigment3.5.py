

def process_text(s):
    length = len(s)
    if s == 0:
        raise ValueError
    dictionary = {}
    dictionary[0] = ("length", length)
    number_of_vowels = 0
    for i in range(length):
        if s[i].lower() in ('a', 'e', 'i', 'o', 'u'):
            number_of_vowels += 1
    dictionary[1] = ("vowels", number_of_vowels)
    uppercase_letters = [letter for letter in s if letter.isupper()]
    dictionary[2] = ("uppercase_letters", uppercase_letters)
    word_lengths = [len(word) for word in s.split()]
    dictionary[3] = ("words_lengths", word_lengths)
    return dictionary
s = "hello my NAME is OR"

def repeat_frame(text, times=3, left='[', right=']'):
    list = []
    for i in range(times):
        list.append(str(left+text+right))
    return list

print(repeat_frame("hello"))