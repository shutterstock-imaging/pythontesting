print("             *((/,")            
print("        ((, (((((((###,")       
print("        #(#(#(((((####(")       
print("               *######( ...")   
print(" (((((((((((##########( ......")
print(".(((((((((############ .......")
print("((((((((#            .......,,")
print(" #(((##  .................,,,,")
print(" /##### .................,,,,")        
print("        .......")               
print("        .........,, .,,")       
print("         ........,, ,,.")
print("     ___       ___      _    ")
print("    | _ \_  _ / __|__ _| |__ ")
print("    |  _/ || | (__/ _` | / _|")
print("    |_|  \_, |\___\__,_|_\__|")
print("         |__/                ")

start = input("\nWelcome to PyCalc, want to begin? ")
if start == ("no"):
    quit()
elif start == ("help"):
    print("num1 = first number, num2 = second number, op = operator")
    print("/ = division, * = multiplication, square = num1 * num1 (ignores num2)")
if start == ("yes"):
    print("OK")

else:
    print("Incorrect Variable")
    quit()

num1 = float(input("Enter num1 "))
op = input("enter an op ")
num2 = float(input("enter num2 "))
if op == ("+"):
    print(num1+num2)
elif op == ("-"):
    print(num1-num2)
elif op == ("*"):
    print(num1 * num2)
elif op == ("/"):
    print(num1/num2)
elif op == ("square"):
    print(num1*num1)
else:
    print("Incorrect Variable")
    quit()