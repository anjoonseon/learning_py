
#price=int(input("물건값을 입력하시오 :")) 물건값 int형으로 입력
#a=int(input("10000원짜리 지폐개수 : ")) 가지고있는 10000원권 입력
#b=int(input("1000원짜리 지폐개수 : "))가지고있는 1000원권 입력
#c=int(input("500원짜리 동전개수 : "))가지고있는 500원권 입력
#d=int(input("100원짜리 동전개수 : "))가지고있는 100원권 입력
#x=a*10000+b*1000+c*500+d*100 가지고있는 돈의 총 합을 x에 대입
#print("반환되는 값 1000원 :",(x-price)//1000,"500원:",((x-price)%1000)//500 ,"100원 :",(((x-price)%1000)%500)//100, "10원 :",((((x-price)%1000)%500)%100)//10,"1원 :",((((x-price)%1000)%500)%100)%10)

#a=10
#b=20
#c=30
#d=40

#a,b=b,a #a,b 값 바뀜
#a,b,c,d=d,c,b,a # 마찬가지로 값 바뀜
#print(a,b,c,d) #결과값 40 30 10 20 출력

#a=10
#b=20
#c=30
#d=40

#if(a>b):
#    print("a가 큽니다.") #if문을 쓸때는 if(조건식):후 내용 입력
#else:#파이썬에서는 같은 블록에 있어야 연결됨 if,,, else,,,
#    print("b가 더 큽니다.")

#import turtle

#t=turtle.Pen()

#while True:#무한반복
#    direction=input("왼쪽=left, 오른쪽=right ")
#    if direction=="left":
#        t.left(60)#60도 왼쪽 회전(머리기준)
#        t.forward(50)#앞으로 50만큼
#    if direction=="right":
#        t.right(60)#60도 회전(오른쪽
#        t.forward(50)

#a=0
#while a<10: while 조건문:
#    num=int(input("정수를 입력하시오 : ")) #정수형으로 num에 입력
#   #num=input("정수를 입력하시오 : ")#아래와같이 해도 됨
#   #num=int(num)
#    if (num%2==0):#2로 나눈 나머지가 0이면 짝수
#        print("짝수")
#    else:#아니면 홀수
#        print("홀수")
#    a+=1 #a++

#buy=int(input("구입 금액 : ")) #100000원 보다 많이샀으면 5%할인된 금액 적용
#if(buy>100000):
#    buy=buy*0.95
#print(buy)

#grade_1=int(input("이수한 학점수를 입력하십시오 : "))
#grade_2=float(input("평점을 입력하십시오 : "))
#if(grade_1>=140 and grade_2>=2.0):#&&이나 ||대신 and나 or사용
#    print("졸업 가능합니다")
#else:
#    print("졸업이 힘듭니다.")
#ctrl+k 후 ctrl c # 선택한 범위 주석

#import datetime #datetime 을 불러옴 (#include와 비슷)

#now=datetime.datetime.now() #datetime에서 now불러옴

#print(now.year,"년")
#print(now.month,"월")
#print(now.day,"일")
#print(now.hour,"시")
#print(now.minute,"분")
#print(now.second,"초")

#if 3<=now.month<=5:
    #print("이번달은 {}월로 봄입니다!".format(now.month))#동시에 여러개의 조건 넣을수있음

#if 6<=now.month<=8:
    #print("이번달은 {}월로 여름입니다!".format(now.month))

#if 9<=now.month<=11:
#    print("이번달은 {}월로 가을입니다!".format(now.month))

#if now.month==12 or 1<=now.month<=2:
#    print("이번달은 {}월로 겨울입니다!".format(now.month))

#import random
#from random import randint rand에서 randint만 가져옴