import string 
while(True):
    guess = input("Enter a single character ")
    if len(guess) == 1 and (guess in string.ascii_lowercase or guess in string.ascii_uppercase):
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

