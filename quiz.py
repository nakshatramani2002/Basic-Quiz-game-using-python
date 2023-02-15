print("welcome to computer quiz")
playing = input("Do u want to play? ")
if playing.lower() != "yes":              #converting to lower cases by using .lower
    quit() 

print("Okay! let's play ")
score = 0                                #initializing with 0
answer= input("What does cpu stand for? ")
if answer.lower() =="central processing unit":
    print("correct")
    score += 1                          #incrementing the score 
else:
    print("incorrect")
answer= input("What does ram stand for? ")
if answer.lower() =="random access memory":
    print("correct")
    score +=1
else:
    print("incorrect")
answer= input("What is psu stand for ? ")
if answer.lower() =="power supply":
    print("correct")
    score +=1
else:
    print("incorrect")
answer= input("What does rom mean ? ")
if answer.lower() =="read only memory":
    print("correct")
    score +=1
else:
    print("incorrect")
answer= input("What does gui stand for? ")
if answer.lower() =="graphic user interface":
    print("correct")
    score +=1
else:
    print("incorrect")
    
print("You got "+ str(score)+ " questions correct!")
print("You have secured "+ str((score /5) * 100) + " percent!")
