president = []
with open("c:\\dd\\pp.txt", "r", encoding="utf8") as f:
    for i in range(5):
        president.append(f.readline().split())

    for i in range(len(president)):
        president[i][1] = int(president[i][1])


    print(" ** 원 본 ** ")
    for i in range(len(president)):
        print(president[i][0], " ====> ", president[i][1])


## 파일 출력 
with open("c:\\dd\\ppout.txt", "a") as f2:

    f2.write(" ** 원 본 ** n\n")
    for i in range(len(president)):
        f2.write(president[i][0])
        f2.write("\t")
        f2.write(str(president[i][1]))
        f2.write("\n")
