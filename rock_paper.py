import random

user_point =0
computer_point =0

variable = ["rock", "paper", "scissors"]

for _ in range(5):
    print("Enter the input: ")
    user_input=input("Choose rock, paper, scissors: ")

    if user_input not in variable:
      print("Invalid choice. Choose something among rock,, paper, scissors")
      continue

    computer_input = random.choice(variable)
    print(f"Computer input : {computer_input}")

    if user_input == "rock":
        if computer_input =="rock":
          print("Its a tie hehe")
        elif computer_input =="paper":
          print("Oops!!Computer got 1 point.")
          computer_point +=1 
        else:
         print("You got 1 point.")
         user_point +=1
     
    elif user_input == "paper":
        if computer_input =="paper":
         print("Its a tie hehe")
        elif computer_input =="scissors":
         print("Oops!!Computer get 1 point.")
         computer_point +=1
        else :
         print("You get 1 point.")
         user_point +=1
     
    elif user_input == "scissors":
        if computer_input =="scissors":
         print("Its a tie hehe")
        elif computer_input =="rock":
         print("Oops!!Computer get 1 point.")
         computer_point +=1 
        else:
         print("You get 1 point.")
         user_point +=1

print(f"Scores -> User: {user_point}, Computer: {computer_point}")
if user_point >  computer_point:
    print("You are the winner <3")
elif user_point < computer_point:
     print("Compuer is the winner. Sigh!!!")
else:
    print("Its a tie tadaaaaa:3")

     
  
