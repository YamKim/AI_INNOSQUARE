class Date(object):
	def __init__(self, year, month):
		self.year = year
		self.month = month
		print(" Date __init__")
	def __del__(self):
		print(" Date __del__")

	def __str__(self):
		return " {}년{}월".format(self.year, self.month) 

class Smart(Date):
	# 이건 자동적으로 호출되지 않고, 추가로 호출 해줘야함.
	cnt = 0
	# 4개의 키워드 중, 부모 클래스에 year, month를 넘기고 나머지를 처리.
	def __init__(self, year, month, model, price):
		#super()키워드는 부모 클래스를 대신한다.
		#단, 부모 클래스를 사용할경우, self를 사용 
		#Date.__init__(self, 2000, 12)
		super().__init__(year, month)

		Smart.cnt += 1
		self.model = model
		self.price = price
		print(" Smart __init__")

	def __del__(self):
		print(" Smart __del__")
		super().__del__()

	# instance를 출력할 때 가지고 있는 값
	def __str__(self):
		return " 모델: {} 가격 : {}만원".format(self.model, self.price)
	def __gt__(self, other):
		print(" 왼쪽이 더 큼")
	def __add__(self, other):
		self.value = self.value + other
	
	def GetModel(self):
		return self.model
	def GetPrice(self):
		return self.price
	def SetModel(self, _model):
		self.model = _model
	def SetPrice(self, _price):
		self.price = _price

	def Disp(self):
		print(" 모델: {} 가격: {}원, {}년{}월 생산".format(self.model, self.price, self.year, self.month))

	'''
	@staticmethod
	def GetCnt1():
		return Smart.cnt

	@classmethod
	def GetCnt2(cls):
		return Smart.cnt
	'''

'''
print(" staticmethod ==> ", Smart.GetCnt1())
print(" classmethod  ==> ", Smart.GetCnt2())

print(" staticmethod ==> ", Smart.GetCnt1())
print(" classmethod  ==> ", Smart.GetCnt2())

s1.Disp()
s2.Disp()
# s1의 ID와 s2의 ID가 같은지 확인하는 method
print(s1.__eq__(s2))

s1.SetPrice(1420000)
s1.Disp()
'''

s1 = Smart(2020, 11, "갤럭시20", 120)
s2 = Smart(2017, 11, "갤럭시11", 80)
s1.Disp()
s2.Disp()
