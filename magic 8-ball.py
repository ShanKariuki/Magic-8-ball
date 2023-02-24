import random
#declaring variables:
name="Shan"
question="will I get filthy rich?"
answer=""
random_number=random.randint(1, 15)
#generates random number between 1 and 15(both inclusive)
#print(random_number)
if random_number == 1:
  answer ="Yes-definitely"
elif random_number == 2:
  answer ="It is decidely so"
elif random_number == 3:
  answer="Without a doubt"
elif random_number == 4:
  answer ="Reply hazy,try again"
elif random_number == 5:
  answer ="Ask again later"
elif random_number == 6:
  answer ="Better not tell you now"
elif random_number == 7:
  answer ="My sources say no"
elif random_number == 8:
  answer ="Outlook not so good"
elif random_number == 9:
  answer ="Very doubtful"
elif random_number == 10:
  answer = "Oh absolutsely"
elif random_number == 11:
  answer ="Mmmmmh no!"
elif random_number == 12:
  answer = "Haha you wish"
elif random_number == 13:
  answer = "Yaaaaaas"
elif random_number == 14:
  answer = "But ofcourse"
elif random_number == 15:
  answer = "In the next life maybe"
else:
  answer = "Error"
print(name +" " + "asks:" + question)
print("magic 8-Balls's answer:" + answer)

if name == " ":
 print("Question" + question)
else:
  print(name+" " + "asks:" + question)
if question == "":
  print("The magic 8-Ball cannot provide a fortune unless you ask it something.")
else:
    print(name +" "+"asks:" + question)
    print("magic 8-ball's answer:" + answer)  

 







