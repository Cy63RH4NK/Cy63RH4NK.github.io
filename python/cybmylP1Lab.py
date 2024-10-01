# CTI 110
# M1LAB - My First Program
#CyberMH
#9/24/2024

#example of formatting
#comments are # or triple quotes

print("Newline\n is kind of like \n<br>\n")
print("\tTabs space out \t\twords")
print("\\ is the backslash")
print("Hello!")

# greet the user by name
# TODO: ask their name
print("What's your name?")
print("Enter first name:")
first = input()
print("enter last name:")
last = input()

#say their name
print("Nice to meet you, ", first, last)

# ask them if they like stuff
print("what do you like?")
topic = input()
print("cool<3 I like", topic, "too.")

#ask them what do they know about dragonball z
print("do you know the original name of planet vegeta?")

# Store the correct answer
real_name_of_vegeta = "Planet Plant"

# Ask the user to input their answer
answer = input("What is the real name of Planet Vegeta? ")

# Compare the user's input with the correct answer and provide feedback
if answer == "Planet Plant":
    print("Well done! You know your Dragon Ball trivia.")
else:
    print(f"Sorry, that's not correct. The real name of Planet Vegeta is Planet Plant.")
    


    

