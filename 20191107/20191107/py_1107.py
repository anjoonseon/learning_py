#1961028 안준선
#1장
print(1+1)#c와는 달리 print라는 함수를 사용하여 내용을 출력한다
print(52,273,"Hello")#','로 동시에 출력 가능하다.
print(1,'\n',2)#중간에 '\n'을 입력함으로써 줄을 바꿔서 출력이 가능하다.
print(5678,'\n',1234,sep='                  ')#sep='  '으로 간격 형성이 가능하다
print("Hello World")#Hello World 출력
#2장
a=2#변수a에 값 2 대입
print(a)#변수 a 출력
a="asdfadfafd"#변수a에 "asdfadfafd"입력(a에 문자열(string)형식으로 넣기때문에 예시와 같이 넣을 수 있음)
print(a)#변수 a 출력
a=1.23456789#a에 숫자(실수형)대입
print(a)#변수 a 출력
a='a'#변수 a에 'a'대입
print(a)#변수 a 출력
a=input()#input()=입력되는 모든 값을 문자로 인식
print(type(a))
print(a+ '1234')#문자 뒤 1234 출력
a=int(input())#int형으로 변환
print(a)
print(a+1234)#입력한 숫자와 1234를 +연산
#"와 ' 표기
#print(""안녕하세요"라고말했습니다")->오류
print('"안녕하세요"라고 말했습니다')#안에 "를 쓰고싶을때는 '사용
print("'배가 고픕니다'라고 생각했습니다.")#반대로 '를 사용하고싶을때는 "사용
print("asdf"*3)#asdf 3번 출력
print("""\
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세\
""")#"""\=>줄을 바꿔 출력하지 않겠다고 선언
#  \" > 큰따옴표   \' > 작은따옴표
#문자선택연산자
print("안녕하세요"[0])#예문처럼 안녕하세요를 출력했을때 5글자이므로 크기 5인 배열이라고 보고 0번째 출력
print("안녕하세요"[1])#마찬가지로 1번째
print("안녕하세요"[2])#2번째
print("안녕하세요"[3])#3번째
print("안녕하세요"[4])#4번째
alp='abcdefghijklmnopqrstuvwxyz'#alp에 'abcdefghijklmnopqrstuvwxyz'대입
print(alp[5:11])#f~k출력
print(alp[18:26])#s~z출력
print(alp[-26:-7])#a~s출력
print(len(alp))#배열의 길이(크기)출력
a=15#a에 15 대입
b=8#b에 8대입
print(a+b,a-b,a*b,a/b,a%b)#사칙연산, 나머지연산 출력
print(a//b)#몫만 출력됨
print(a**b)#제곱
a=input()
print(a)
#파이썬은 변수 선언시 정의(값)도 입력해주어야된다.
tmp=''
for i in alp:
    tmp+=i
    print(tmp)#파이썬 안의 for문
a=input("숫자를 입력하세요 : ")#scanf,printf동시에 가능
a=4.123
