import random

choices =["rock", "paper", "scissors"]

computer = random.choice(choices)
man = input("please enter your choice : ")

if(man == computer):
    print("computer choice : ",computer)
    print("its a tie oof")
if(man=="rock" and computer=="scissors"):
    print("computer choice : ", computer)
    print("you win!")

if(man=="rock" and computer=="paper"):
    print("computer choice : ", computer)
    print("you lose!")
if(man=="scissors" and computer=="rock"):
    print("computer choice : ", computer)
    print("you lose!")
if(man=="scissors" and computer=="paper"):
    print("computer choice : ", computer)
    print("you win!")
if(man=="paper" and computer=="rock"):
    print("computer choice : ", computer)
    print("you win!")
if(man=="paper" and computer=="scissors"):
    print("computer choice : ", computer)
    print("you lose!")
