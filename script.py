import random
def reverse_string(word):
    word = word[:: -1]
    return word
non_alphabetical_chars = [
    "!", "@", "#", "$", "%", "^", "&", "*", "_",
    "=", "+", 
    "<", ">", ".", "?",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]


length = 8 

random_chars_list = random.choice(non_alphabetical_chars)
random_chars_list2 = random.choice(non_alphabetical_chars)

print(random_chars_list2)

random_char = random_chars_list

print("Enter your name, place of birth or current location.")

password = input()
password = random_char.join(random.sample(password, len(password)))

password = "".join(random.sample(password, len(password)))[::-1]
password = password.strip(password.replace(random_chars_list, random_chars_list2))





print(password)



# print(name)


