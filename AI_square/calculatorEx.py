#간단 계산기 

from mymodule import *

if __name__ == "__main__":
    print(" calculatorEx main ===================== ")

while True:
    print(" 간단 계산기 [Quit:0]  ")
    number1 = int(input(" 첫 번째 수 : "))
    if number1 == 0:
        print(" 프로그램 종료... \n")
        break
    op = input(" [ +, -, *, / ] : ")
    number2 = int(input(" 두 번째 수 : "))

    if op == '+':
        res = Plus(number1, number2)
    elif op == '-':
        res = Minus(number1, number2)
    elif op == '*':
        res = Multi(number1, number2)
    elif op == '/':
        res = Divi(number1, number2)
    else:
        print(" {}연산은 없어요..".format(op))
        continue

    print(" 결과 : {} {} {} = {} \n".format(number1, op, number2, res))
    
