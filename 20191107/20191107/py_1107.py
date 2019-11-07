#1장
print(1+1)
print(52,273,"Hello")
print(1,'\n',2)
print(5678,'\n',1234,sep='                  ')
print("Hello World")
#2장
a=2
print(a)
a="asdfadfafd"
print(a)
a=1.23456789
print(a)
a='a'
print(a)
a=input()
print(type(a))
print(a+ '1234')
a=int(input())
print(a)
print(a+1234)
#"와 ' 표기
#print(""안녕하세요"라고말했습니다")->오류
print('"안녕하세요"라고 말했습니다')
print("'배가 고픕니다'라고 생각했습니다.")
print("asdf"*3)
#문자선택연산자
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])
alp='abcdefghijklmnopqrstuvwxyz'
print(alp[5:11])#f~k
print(alp[18:26])#s~z
print(alp[-26:-7])#a~s
print(len(alp))
a=15
b=8
print(a+b,a-b,a*b,a/b,a%b)
print(a//b)#몫만 출력됨
print(a**b)#제곱
a=input()
print(a)
#파이썬은 변수 선언시 정의(값)도 입력해주어야된다.
tmp=''
for i in alp:
    tmp+=i
    print(tmp)
a=input("숫자를 입력하세요 : ")#scanf,printf동시에 가능
a=4.123