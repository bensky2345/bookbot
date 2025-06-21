# Function to count the number of words 
def num_of_words(text):
    number_words = len(text.split())
    return number_words

# Function to check if the char is in the dictionary, converts it to lowercase to avoid duplicates, and increment if its found
# if not, it will be added to the dictionary 
def char_appears_count(text):
    char_count_dict = {}
    for char in text:
        char = char.lower()
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1

    return char_count_dict

def sorted_char_dict(chars):
    return chars["num"]

# Function used for sorting from highest to lowest. Initiated a list
# so that I can use the .sort() function 
def sorting(char_count_dict):
    dict_list = []
    for chars in char_count_dict:
        # For checking if the character is alphabet, if not, skip. The char_dict dictionary
        # is used to save the key and value of char(key) and num(value)
        # then save it tho the list by using the .append() command
        if chars.isalpha():
            char_dict = {"char": chars, "num": char_count_dict[chars]}
            dict_list.append(char_dict)
        else:
            pass
    
    dict_list.sort(reverse=True, key=sorted_char_dict)

    return dict_list
