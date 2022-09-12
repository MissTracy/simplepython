import operators


print("Hello!")
print("Please select an operation.")
print("")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("")

tmp = operators.formulerss()


while True:
    choice = input("Please make your selecection (1-2-3-4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        if choice == '1':
            print(num1, "+", num2, "=" , tmp.add(num1,num2))

        elif choice == '2':
            print(num1, "-", num2, "=", tmp.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", tmp.multiply(num1,num2))

        elif choice == '4':
            print(num1, "/", num2, "=", tmp.divide(num1,num2))
        
        continue_calc= input("Would you like to do another calculation? (yes/no): ")
        if continue_calc == "no":
          break
    
    else:
        print("Invalid Input")