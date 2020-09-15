### file I/O
```python
# file read
fileName = "./files"
fp = open(fileName, "r")
fp.read()
fp.close()

with open("~경로~", "r", encoding='utf') as f:
	for i in range(10):
		a.append(f.readline().split())
```
```python
# file write
fp = open(fileName, "w", encoding='utf8')
fp.write("add string")
fp.close()
```

### 진수처리
```python
>>> bin(10)
'0b1010'
>>> oct(10)
'0o12'
>>> hex(10)
'0xa'
```

### 복소수 개념
```python
>>> a = 4 + 4j
>>> print("real: %d, imag: %d" % (a.real, a.imag))
```

### 문자열 처리
```python
>>> a = 'apple'
>>> a.count('p')
2
>>> a.find('e')
4
```
count: apple 내에 p의 개수를 구하기
find: apple 내의 e가 몇번째인지 구하기

### 변수 관리
```python
# dir(): 
dir()
>>> del a, b, c
# a, b, c가 메모리상에서 지워지게 됨
>>> dir(__builtins__)
# builtin 함수들이 나옴
>>> b = 200
>>> b.__add__(50)
# built in 함수를 활용하여 기존 b값에 더한다.
250

```

### encode, decode
```python
>>> char(98)
'0'
>>> ord('B')
66
>>> '\uac00'
'가'
>>> hex(ord('가'))
'0xac00'
>>> type(a.encode())
<class 'bytes'>
```

### list처리
```python
>>> a = [3333, 230, 300, 30, 30]
>>> a.index(30)
3
>>> a.count(30)
2
>>> len(a)
5
>>> a.del(30)

# 복사시에는 할당이 아닌 copy 메소드로해야 주소 공유 안됨
# aa와 a는 서로 다른 주소이므로 수정해도 영향받지 않음.
>>> aa = a.copy()
```

### range처리
```pyhton
# 1부터 2의 간격으로 10 미만인 값들.
for i in range(1, 10, 2):
	~
```

### lambda 함수
```python
# 특정 주소에 함수를 만들고 그 함수를 호출하여 사용
# filter 사용 예시
>>> f3 =  lambda x : x % 2
# f3의 조건을 만족(1이 되는)하는 원소를 나열.
>>> list(filter(f3, range(1, 8)))
[1, 3, 5, 7]

# map 사용 예시
>>> f2 = lambda x : x * x
>>> b = [1, 2, 3, 4, 5]
>>> list(map(f2, b))
>>> [1, 4, 9, 16, 25]
```

### Class 처리
객체 object  
인스턴스 instance  
생성자 __init__  
소멸자 __del__  
magic method  
상속 inheritance  
부모 super(), 자식  
staticmethod, classmethod  
접근 지정 - 공개, 반공개, 비공개  



### MySQL
```
DB 관련 -------------------------
DB 생성 
> CREATE DATABASE exDB;
DB 확인
> SHOW DATABASES;
DB 선택
> USE exDB;
DB 삭제
> DROP DATABASE exDB;

TABLE 관련 ---------------------
현재 DB안에 있는 전체 TABLE 보기
> SHOW TABLES;

TABLE 생성
> CREATE TABLE exTB(
-> KOR INT,
-> ENG INT,
-> );

값 추가
> INSERT INTO score(name, kor, eng) values("아이유", 90, 95)
> INSERT INTO score(name, kor, eng) SELECT name, kor, mat FROM score2

값 변경
> UPDATE score
-> SET eng = 100
-> WHERE name = '아이유';

값 삭제
> DELETE FROM score WHERE kor <= 50;

필터
> SELECT * FROM score WHERE eng >= 90;
> SELECT * FROM score WHERE eng <> 90;		// <>는 같지 않을 때를 의미
> SELECT * FROM score WHERE name LIKE '%유'
> SELECT * FROM score WHERE kor in(90, 85, 70);
> SELECT * FROM SCORE ORDER BY kor ASC;		// 국어점수에 따라 오름차순으로 정렬
> SELECT * FROM SCORE ORDER BY kor DESC;	// 국어점수에 따라 내림차순으로 정렬

열 다루기
추가
> ALTER TABLE score ADD total int;
삭제
> ALTER TABLE score DROP total; 


```

### sqlite3
table 생성
> create table score (
> name char(20),
> kor int,
> eng int,
> mat int);
# table 확인
> .table

# 헤더 추가
> .header on
# col 공백으로 나누기
> .mode column
# table 불러오기
> select * from sccore;
# 외부 파일 불러오기
> .import "경로" table명
# 행 추가하기
> insert int score values("아이유", 90, 95, 95);

# d드라이브에 dd라는 db 생성
> .open d:\\dd
# Man이라는 table이 존재하면 제거하고 새로 생성  
> DROP TABLE IF EXISTS Man;
# Man table을 생성
CREATE TABLE Man(name char(20), age int);
