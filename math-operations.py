
while True:
  list = ["add", "subtract", "Exit"]
  print(list)
  question = input("choose 1: ")
  if question == "add":
    num1 = int(input("add a number: "))
    num2= int(input("add another number: "))
    answer = num1 + num2
    print(answer)
  if question == "subtract":
    num1 = int(input("subtract a number: "))
    num2= int(input("subtract another number: "))
    answer = num1 - num2
    print(answer)
  if question == "Exit":
    break
