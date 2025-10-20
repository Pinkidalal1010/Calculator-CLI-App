#calculator
def add(a,b):
    return a+b
 

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if(b==0):
        return "Error Division by zero is not possible!"
    else:
        return a/b
    
def main():
    print("--- Simple  CLI Calculator ")
    while True:
        print("Select operation  ")
        print("1. ADD +")
        print("2. Subtract -")
        print("3. Multiply *")
        print("4 . divide /")

        print("5. Exit")
        choice = input("Enter your choice(1-5): ")
        if(choice == '5'):
            print("Exiting.... Thank You!")
            break 
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if(choice == '1'):
            print("Result:",add(num1,num2))
        elif(choice == '2'):
            print("Result:",subtract(num1,num2))
        elif(choice == '3'):
            print("Result:",multiply(num1,num2))
        elif(choice == '4'):
            print("Result:",divide(num1,num2))
        else:
            print("Invalid input! Please choose between 1-5.")
if __name__=="__main__":
    main()