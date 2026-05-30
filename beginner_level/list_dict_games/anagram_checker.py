# Determine if two strings are anagrams of each other.

# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Examples of Anagrams
# "Listen" -> "Silent"
# "Earth" -> "Heart"
# "Dormitory" -> "Dirty room"
# "The Morse Code" -> "Here come dots"

def anagram_checker(str_1, str_2):
    output = False
    dict_str_1 = dict()
    dict_str_2 = dict()
    # loop through string 1
    for i in str_1:
        if i != " ":
            if i in dict_str_1:
                dict_str_1[i] += 1
            else:
                dict_str_1[i] = 1

    # loop though string 2
    for i in str_2:
        if i != " ":
            if i in dict_str_2:
                dict_str_2[i] += 1
            else:
                dict_str_2[i] = 1

    if dict_str_1 == dict_str_2:
        output = True
    return output

while True:
    str_1 = input("Enter the first string : ").lower()
    str_2 = input("Enter the second string : ").lower()
    print(f"Are both strings Anagrams? : {anagram_checker(str_1, str_2)}")

    query = input("Do you want to continue? (y/n) ").lower()
    if query == 'n':
        break