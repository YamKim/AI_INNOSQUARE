try:
    a = [1, 2, 3]
    #a[4] = 5
    #4 / 0
    #print(a.__next__()
    "서울" + 4

except ZeroDivisionError:
    print("0으로 나누면 안됨")

except IndexError:
    print("범위 벗어남")

except TypeError:
    print("타입 다름")

except  SyntaxError:
    print("문법 오류")

except:
    print("그 외의 에러")

finally:
    print("무조건 실행되는 구문")
