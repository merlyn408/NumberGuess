import random
chances=7
print("Enter lower bound: ")
a=int(input())
print("Enter upper bound: ")
b=int(input())
choice=random.randrange(a,b)
guess=0
while guess<chances:
  guess+=1
  print("Guess the number!")
  ch=int(input())
  if ch==choice:
    print("Yay! The number is",choice,"You got it right in the",guess,"attempt")
    break
  elif guess>=chances and ch!=choice:
    print("Sorry! The number is",choice,"Better luck next time")
  elif ch>choice:
    print("The number is too high! Guess a smaller number")
  elif ch<choice:
    print("The number is too less! Guess a bigger number")
  