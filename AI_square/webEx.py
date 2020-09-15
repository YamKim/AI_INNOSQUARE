import webbrowser as wb
import sys


while True:
    print(" 1. naver.com ")
    print(" 2. google.com ")
    print(" 3. daum.net ")
    print(" 4. youtube.com ")
    print(" 0. Quit ")
    a = input(" 열고 싶은 웹: ")

    if a == 1:
        wb.open("naver.com")
    elif a == 2:
        wb.open("google.com")
    elif a == 3:
        wb.open("daum.net")
    elif a == 4:
        wb.open("youtube.com")
    elif a == 0:
        sys.exit
    else:
        break
