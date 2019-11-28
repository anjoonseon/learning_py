#classCounter: 
#	defreset(self): 
#		self.count= 0   # 인스턴스변수 
#		defincrement(self): 
#			self.count+= 1 
#		defget(self): 
#			return self.count #counter클래스
#a = Counter()
#a.reset()
#a.increment() 
#print("카운터a의값은", a.get() # 객체생성
#a = Counter() 
#b = Counter()
#a.reset() 
#b.reset() #객체 2개 생성
#t = Television(9, 10, True)
#t.show() t.setChannel(11) t.show() #메소드호출
#class Student: 
#	def__init__(self, name=None, age=0): 
#		self.__name= name   #private으로정의, 내부에서만접근가능 
#		self.__age= age
#obj=Student() 
#print(obj.__age) #정보은닉
#import math 
#class Circle: 
#	def __init__(self, radius=1.0): 
#		self.__radius= radius
#	def setRadius(self, r): 
#		self.__radius= r
#	def getRadius(self): 
#		return self.__radius
#	def calcArea(self): 
#		area = math.pi*self.__radius*self.__radius 
#		return area 
#	def calcCircum(self):
#	   circumference = 2.0*math.pi*self.__radius 
#	   return circumference
#c1=Circle(10)
#print("원의반지름=", c1.getRadius()) 
#print("원의넓이=", c1.calcArea()) 
#print("원의둘레=", c1.calcCircum()) #원을 클래스로 표현