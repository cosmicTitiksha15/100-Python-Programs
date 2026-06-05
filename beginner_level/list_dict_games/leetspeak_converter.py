# Replace standard letters with numbers (e.g., 'e' -> '3', 'a' -> '4')
# Standard Text: leet hacker
# Leetspeak Conversion: l33t h4ck3r
# letter -> number conversion

def leetspeak_converter(paragraph):
    dict_conversion = {
        'A' : 4,
        'B' : 8,
        'E' : 3,
        'F' : 7,
        'G' : 9,
        'I' : 1,
        'O' : 0,
        'Q' : '(,)',
        'S' : 5,
    }
    list_paragraph = list(paragraph)
    leet_list = []
    print(list_paragraph)
    for i in list_paragraph:
        if i in dict_conversion:
            i = dict_conversion[i]
            leet_list.append(str(i))
        else:
            leet_list.append(i)
            

    paragraph = ''.join(leet_list)
    return paragraph

while True:
    query = input("Enter the string : ").strip().upper()
    result = leetspeak_converter(query)
    print(f"Leetspeak conversion: {result}")

    y_n = input("Do you want to continue: (y/n) ").lower()
    if y_n == 'n':
        break