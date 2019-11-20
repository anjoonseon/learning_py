#statement=input("문자열을 입력하시오: ") #문자열 조사

#alphas=0
#digits=0
#spaces=0

#for c in statement:
#   if c.isalpha(): #isalpha함수 사용해서 알파벳 개수 확인
#      alphas=alphas+1
#   if c.isdigit(): #isdigit함수 사용해서 숫자 개수 확인
#      digits=digits+1
#   if c.isspace(): #isspace함수 사용해서 공백 개수 확인
#      spaces=spaces+1
#print("알파벳 문자의 개수=",alphas)
#print("숫자 문자의 개수=",digits)
#print("스페이스의 개수=",spaces)

#def get_sum(start, end): #1부터10까지 함수
#   sum=0
#   for i in range(start, end+1):
#      sum+=i #sum에 start~end+1을 더함
#   return sum #sum반환

#value = get_sum(1,10) #start값을 1로, end+1값을 10으로 지정
#print(value) #결과값출력(55)


#def get_sum(start, end): #함수
#   sum=0
#   for i in range(start, end+1):
#      sum+= i
#   print(sum)

#value = get_sum(1,10)
#print(value)

#def asterisk_test(a,b,*args):
#    return a+b+sum(args)

#print(asterisk_test(1,2,3,4,5)) #안의 수들의 합 출력

#참조에 의한 호출, 값에 의한 호출 알아두기