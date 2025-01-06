print("RULES OF THE GAME ARE :-")
print("YOU HAVE ONLY FIVE CHANCES !!")
print("enter the number between 0,1,2")
print("0 stands for snake , 1 stands for water, 2 stands for gun")

count = 1
while count<=5:
      import random

      def check(comp,user):
          if comp == user:
             return 0
          if(comp == 0 and user==  1):
             return -1
          if(comp == 0 and user == 2):
             return -1
          if(comp == 2 and user == 0):
             return -1
          else:
             return 1

      user = int(input("enter between (0,1,2):"))
      comp = random.randint(0,2)
      print("you entered:",user)
      print("the computer entered:",comp)

      score = check(comp,user)
      if score == 0:
          print("it's a draw")
          if count == 4:
              print("LAST CHANCE COME ON!!!!")
      elif score == -1:
          print("you lose!")
          if count == 4:
              print("LAST CHANCE COME ON!!!")
      elif score == 1:
          print(" hurray you won!!!!")
          break
          if count == 4:
              print("LAST CHANCE COME ON!!!")

      count = count+1
print("all the chances are over********")
