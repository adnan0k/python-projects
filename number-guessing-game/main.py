import random

print('hello world, lets guess numbers!!!')

rand = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
user_inp = int(input("Take a guess: "))

for val in range(0,3):
    if(user_inp == rand):
        print("congratulations you have guessed the right number!")
        break
    elif(user_inp > rand):
        print("Too High!")
        user_inp = int(input("Take a guess again: "))
    elif(user_inp < rand):
        print("Too low!")
        user_inp = int(input("Take a guess again: "))
        
if(user_inp != rand):
    print("The correct number was: " + str(rand))