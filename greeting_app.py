#Create a program that asks for the user’s name and favorite color, then prints a personalized greeting like: “Hello, [Name]! Your favorite color, [Color], is awesome!”

def greeting_app():
# Prompt the user for their name
    name = input("What is your name? ")
# Prompt the user for their favorite colour
    colour = input("What is your favorite colour? ")
    
# Print a personalized greeting
    print(f"Hello, {name}! Your favorite colour, {colour}, is awesome!")

#run the function
greeting_app()