print("WELCOME")

play = input("DO YOU WANT TO PLAY?  " )

if play.lower() != "yes":
    quit()

print("GREAT! LETS PLAY :)")
score=0

answer = input("what does CPU stand for? ")
if answer.lower() =="central processing unit":
    print("Awesome!")
    score+=1
else:
    print("oops!!Wrong")

answer = input("what does GPU stand for? ")
if answer.lower() =="graphics processing unit":
    print("Awesome!")
    score+=1
else:
    print("oops!!Wrong")

answer = input("what does RAM stand for? ")
if answer.lower() =="random access memory":
    print("Awesome!")
    score+=1

else:
    print("oops!!Wrong")

answer = input("what does ROM stand for? ")
if answer.lower() =="read only memory":
    print("Awesome!")
    score+=1
else:
    print("oops!!Wrong")

print("You got " + str(score) +" questions correct!" )

