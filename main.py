import add
import Subtract
import Multiply
import Divide

print("Calculator started.")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 
while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        
        if choice == '1':
            print(num1, "+", num2, "=", add.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Subtract.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", Multiply.multiply(num1, num2))
            
        elif choice =='4':
            print(num1, "/", num2, "=", Divide.divide(num1,num2))
            
           
            
       
        # check if user wants another calculation
        # break the while loop if answer is no
        
        while True:
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation in ('y', 'Y', 'yes', 'Yes', 'yEs', 'yeS', 'YEs', 'YeS', 'yES', 'YES','n', 'N', 'no', 'No', 'nO', 'NO'):
                
                break       
                
            else :
                print("Please re-enter.")
                continue
                
        
        f = open("stdout.txt", 'a')
        print(choice, num1, num2, next_calculation,  file=f)
        f.close()
  
        
        if next_calculation in ('y', 'Y', 'yes', 'Yes', 'yEs', 'yeS', 'YEs', 'YeS', 'yES', 'YES'):
            continue
        elif next_calculation in ('n', 'N', 'no', 'No', 'nO', 'NO') :
            check = input("Are you sure? (yes/no): ")
            if check in ('y', 'Y', 'yes', 'Yes', 'yEs', 'yeS', 'YEs', 'YeS', 'yES', 'YES'):
                break
            elif next_calculation in ('y', 'Y', 'yes', 'Yes', 'yEs', 'yeS', 'YEs', 'YeS', 'yES', 'YES'):
                continue
            continue
      
    
    else:
        f = open("stdout2.txt", 'a')
        print("Invalid input : ", choice,  file=f)
        f.close()
   


#commit test
