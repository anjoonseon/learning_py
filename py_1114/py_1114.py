
#import turtle #turtle함수 불러오기

#star=turtle.Turtle()

#for i in range(5): # 5번 반복
#    star.forward(200) # 200만큼 앞으로 이동
#    star.right(144) # 오른쪽으로 144만큼 이동

#import turtle

#t= turtle.Turtle()

#num_sides=int(input("변의 수 입력")) # 위를 응용해서 n각형을 출력하기 (n입력받음)
#side_length=55 #n각형 한 변의 길이를 55로 지정
#angle=360.0/num_sides #angle에 다각형의 각도 지정

#for i in range(num_sides): # range자료형을 사용해서 num_sides-1만큼 반복
#    t.forward(side_length) # 앞으로 side_length만큼 이동
#    t.right(angle) # 오른쪽으로 angle만큼 이동

#i=0 #i에 0 할당
#while i<5: #5번 반복
#    print("환영합니다.") #환영합니다 출력
#    i+=1 #i++
#print("반복종료") #반복종료 출력

#i=1 #i에 1 할당
#while i<10: 10번 반복
#    print(i*3) #i*3출력
#    i+=1 #i++
#num=0 #num에 0할당
#for i in range(3,100,3): 
#    num+=i
#print(num)
#sum=0
#for i in range(0,101,1):
#    sum+=i
#print(sum)
   

#import turtle

#t= turtle.Turtle()

#num_sides=int(input("변의 수 입력")) # 위를 응용해서 n각형을 출력하기 (n입력받음)
#side_length=55 #n각형 한 변의 길이를 55로 지정
#angle=360.0/num_sides #angle에 다각형의 각도 지정
#num_repeat=3
#for a in range(num_repeat):
#    t.right(20)
#    for i in range(num_sides): # range자료형을 사용해서 num_sides-1만큼 반복
#        t.forward(side_length) # 앞으로 side_length만큼 이동
#        t.right(angle) # 오른쪽으로 angle만큼 이동

#num=0 #num에 0할당
#ans=int(input("어떤 배수의 합을 구할까요?"))
#for i in range(0,100,ans): 
#    num+=i
#print(num)

num=int(input("숫자를 입력하세요"))
sum=0;
for i in 1:
    sum+=num//10
    num=num%10
    if(num//10,0):
        break;
    print(sum)

