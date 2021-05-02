import math


def subtraction(var1, var2):
    if var2 > var1:
        swap_a = var1
        var1 = var2
        var2 = swap_a
    answer = var1 - var2
    return answer


def addition(var1, var2):
    answer = var1 + var2
    return answer


def multiplication(var1,  var2):
    answer = var2 * var1
    return answer


def division(var1, var2):
    if var2 == 0 and var1 > 0:
        print("sorry that is an invalid operation,though shall not divide by zero")
    else:
        answer = var1 / var2
        return answer


def square(var):
    answer = var * var
    return answer


while True:
    print('''WELCOME TO THE SCIENTIFIC CALCULATOR
    ----------------------------------------\n
    to perform any operation just choose the type of operation you want to perform
    ------------------------------------------------------------------------------
    1) ADDITION
    2) SUBTRACTION
    3) MULTIPLICATION
    4) DIVISION
    5) FIND THE SQUARE OF A NUMBER
    6) FIND THE SQUARE ROOT OF A NUMBER
    7) COSINE(cos0)
    8) TANGENT(tan0)
    9) SIN(sin0)
    0) EXIT
    ''')
    operation = int(input("enter the operation you want to perform here: "))
    while True:
        if operation == 1:
            print('you have selected the addition operation')
            valuable1 = int(input("enter the first value: \n"))
            valuable2 = int(input("enter the second value\n"))
            print(f'you want to add the following values {valuable1} and {valuable2}\n')
            option = input("press enter to confirm and 0 to exit: ")
            if option == 0:
                break
            elif option == "":
                results = addition(valuable1, valuable2)
                print("=============================================\nyour answer is ", results," \n===================================")
                continuing = input('\ndo you still want to continue adding some numbers enter \n1) continue\n0) to '
                                   'exit\n>: ')
                if continuing == 1:
                    print('\nLET US CONTINUE WITH ADDITION\n')
                elif continuing == 0:
                    print('\nTHANK YOU FOR USING THE CALCULATOR .........\n.............EXITING')
                    break
                else:
                    print("that was not a valid operation,! exiting")
                    break

        if operation == 2:
            print('you have selected subtraction operation')
            valuable1 = int(input("enter the first value: \n"))
            valuable2 = int(input("enter the second value\n"))
            print(f'you want to subtract the following values {valuable1} and {valuable2}\n')
            option = input(f"press enter to confirm or :\n 1) to  subtract {valuable2} from {valuable1}\n 0) to exit :")
            if option == 0:
                break
            elif option == 1:
                swap = valuable1
                valuable1 = valuable2
                valuable2 = swap
                results = subtraction(valuable1, valuable2)
                print("=============================================\nyour answer is ", results,
                      " \n===================================")
                continuing = input('\ndo you still want to continue adding some numbers enter \n1) continue\n0) to '
                                   'exit\n>: ')
                if continuing == 1:
                    print('\nLET US CONTINUE WITH ADDITION\n')
                elif continuing == 0:
                    break
            elif option == "":
                results = subtraction(valuable1, valuable2)
                print("=============================================\nyour answer is ", results,
                      " \n===================================")
                continuing = input('\ndo you still want to continue subtracting some numbers enter\n1) continue\n0) to '
                                   'exit\n>: ')
                if continuing == 1:
                    print('\nLET US CONTINUE WITH ADDITION\n')
                elif continuing == 0:
                    break
        if operation == 3:
            print('you have selected the multiplication operation')
            valuable1 = int(input("enter the first value: \n"))
            valuable2 = int(input("enter the second value\n"))
            print(f'you want to multiply the following values {valuable1} and {valuable2}\n')
            option = input("press enter to confirm and 0 to exit")
            if option == 0:
                break
            else:
                results = multiplication(valuable1, valuable2)
                print("your answer is ", results)
        if operation == 4:
            print('you have selected the division operation')
            valuable1 = int(input("enter the first value: \n"))
            valuable2 = int(input("enter the second value\n"))
            print(f'you want to divide  {valuable1} by {valuable2}\n')
            option = input(f"press enter to confirm or \n1)to divide {valuable2}  by {valuable1}\n0) to exit\n :")
            if option == 0:
                break
            elif option == 1:
                swap = valuable1
                valuable1 = valuable2
                valuable2 = swap
                results = division(valuable1, valuable2)
                print("your answer is ", results)
            else:
                results = division(valuable1, valuable2)
                print("your answer is ", results)
        if operation == 5:
            print('you have selected find the square operation')
            valuable1 = int(input("enter your value here: \n"))
            option = input(f"press enter to confirm and 0 to exit: ")
            if option == 0:
                break

            else:
                results = square(valuable1)
                print("your answer is ", results)
        if operation == 6:
            print('you have selected find the square root operation')
            valuable1 = int(input("enter your value here: \n"))
            option = input(f"press enter to confirm and 0 to exit: ")
            if option == 0:
                break

            else:
                results = math.sqrt(valuable1)
                print("your answer is ", results)
        if operation == 7:
            print('you have selected find the cosine operation')
            valuable1 = int(input("enter your value here: \n"))
            option = input(f"press enter to confirm and 0 to exit: ")
            if option == 0:
                break

            else:
                results = math.cos(valuable1)
                print("your answer is ", results)
        if operation == 8:
            print('you have selected find the tangent operation')
            valuable1 = int(input("enter your value here: \n"))
            option = input(f"press enter to confirm and 0 to exit: ")
            if option == 0:
                break

            else:
                results = math.tan(valuable1)
                print("your answer is ", results)
        if operation == 9:
            print('you have selected find the sin operation')
            valuable1 = int(input("enter your value here: \n"))
            option = input(f"press enter to confirm and 0 to exit: ")
            if option == 0:
                break

            else:
                results = math.sin(valuable1)
                print("your answer is ", results)
        if operation == 0:
            print("")
            break
        else:
            print("Enter a valid numbers")
            break
    else:
        print("enter a valid option to perform the operation!2")
else:
    print("Bye Bye")
