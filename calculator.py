import formulerss

print("Hello!")
print("Please select an operation.")
print("")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("")

while True:
    choice = input("Please make your selecection (1-2-3-4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        if choice == '1':
            print(num1, "+", num2, "=" ,  )

        elif choice == '2':
            print(num1, "-", num2, "=", formulerss.subtract)

        elif choice == '3':
            print(num1, "*", num2, "=", formulerss.multiply)

        elif choice == '4':
            print(num1, "/", num2, "=", formulerss.divide)
        
        continue_calc= input("Would you like to do another calculation? (yes/no): ")
        if continue_calc == "no":
          break
    
    else:
        print("Invalid Input")