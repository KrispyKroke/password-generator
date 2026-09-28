import random 
import math
import string
import sys



def check_Length():  ## method for checking input in regards to desired length of password
    print("How long would you like your password to be? (between 4 to 16 characters)")
    failed = True
    while failed:
        try:
            pw_length = int(input())
        except:
            print("Sorry, please try again!")
            return
        if pw_length < 4 or pw_length > 16:
            print("Password must be between 4 and 16 characters long.")
        else:
            failed = False
    return pw_length
                   

def check_Chars():  ## method for checking input in regards to number of special character types
    print("How many special character types would you like to include? (Between 0 to 2 types)")
    failed = True
    while failed:
        try:
            num_of_chars = int(input())
        except:
            print("Sorry, please try again!")
            return
        if num_of_chars < 0 or num_of_chars > 2:
            print("You are only allowed anywhere from 0 to 2 special character types.")
        else:
            failed = False
    return num_of_chars

def check_Strength(length, chars):  ## method for gauging password strength by checking both length and number of special character types and finding the overall strength from both
    strengths = ["very poor", "poor", "neutral", "good", "very good"]
    length_strength = 0
    char_strength = 0
    if length < 6:
        length_strength = 0
    elif length < 8:
        length_strength = 1
    elif length < 12:
        length_strength = 2
    elif length < 14:
        length_strength = 3
    else:
        length_strength = 4
    if chars == 0:
        char_strength = 1
    elif chars == 1:
        char_strength = 2
    else:
        char_strength = 3
    
    final_avg = (length_strength + char_strength) / 2
    return strengths[math.ceil(final_avg)]



def insert_char(original_string, char_to_insert):   ## method for inserting character at random spot in password string
    random_index = random.randint(0, len(original_string))
    
    return original_string[:random_index] + str(char_to_insert) + original_string[random_index:]




def generate_Password():  ## method for generating the password itself. varies based on length desired and special characters to be included.
    pw_length = check_Length()
    if pw_length == None:
        return
    special_chars = check_Chars()
    if special_chars == None:
        return
    pw_strength = check_Strength(pw_length, special_chars)
    password = ""
    use_punctuation = False
    use_arithmetic = False
    if special_chars >= 1:
        use_punctuation = True
    elif special_chars == 2:
        use_arithmetic = True
    else:
        pass

    pool = string.ascii_letters + string.digits
    arithmetic_operators = "+-*/"

    if use_arithmetic and use_punctuation:
        first_arith = random.randint(0, 3)
        first_punc = random.randint(0, 31)
        pool += "+-*/" + string.punctuation
        password = "".join(random.choices(pool, k = pw_length - 2))
        password = insert_char(password, arithmetic_operators[first_arith])
        password = insert_char(password, string.punctuation[first_punc])
    elif use_punctuation:
        first_punc = random.randint(0, 31)
        pool += string.punctuation
        password = "".join(random.choices(pool, k = pw_length - 1))
        password = insert_char(password, string.punctuation[first_punc])
    else:
        password = "".join(random.choices(pool, k = pw_length))

    return [password, pw_strength]




            




def main():  
    print("Welcome! I see you are in need of a password. Take heed of the following prompts to find your perfect password! Type quit if you'd like to exit the program or any other key to continue.")
    exit_prompt = input()
    if exit_prompt == "quit":
        sys.exit()
    else:
        pass
    data = generate_Password()
    if data == None:
        return
    print("Here is your password: " + data[0] + " and its relative strength: " + data[1])

while 1:
    main()