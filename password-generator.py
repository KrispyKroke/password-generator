import random 




def check_Length():
    print("How long would you like your password to be? (between 4 to 16 characters)")
    failed = True
    while (failed):
        pw_length = input()
        if (isinstance(pw_length, int)):
            if (pw_length < 4 or pw_length > 16):
                print("Password must be between 4 and 16 characters long.")
            else:
                failed = False
        else:
            print("Please enter a number between 4 and 16.")
    return pw_length
                   

def check_Chars():
    print("How many special characters would you like to include? (Between 0 to 3 types)")
    failed = True
    while(failed):
        num_of_chars = input()
        if (isinstance(num_of_chars, int)):
            if (num_of_chars < 0 or num_of_chars > 3):
                print("You are only allowed anywhere from 0 to 3 special character types.")
            else:
                failed = False
        else:
            print("Please enter a number between 0 and 3.")
    return num_of_chars

def check_Strength():



def generate_Password():
    pw_length = checkLength()
    special_chars = check_Chars()
    pw_strength = check_Strength()

            




def main():
    print("Welcome! I see you are in need of a password. Take heed of the following prompts to find your perfect password!")
    generate_Password()


main()