# 함수
# 함수정의 - 이건 실행이 아님
# 함수만드는 방법 4가지
# 1. 파라미터O 리턴O
# 2. 파라미터O 리턴X
# 3. 파라미터X 리턴O
# 4. 파라미터X 리턴X
def add(x,y):  # 함수종류의 2번째
    result = x + y
    print(result)

def sub(x,y):
    result = x - y
    print(result)

def mul(x,y):
    result = x*y
    print(result)
    
def div(x,y):
    result = x/y
    print(result)
    
def hello():    #()안에 있는 것이 파라미터, 파라미터 없이 리턴안하는것 4번째
    print('Hello~!!')
    
def hello2():  #함수종류의 3번째
    msg = 'Hello, Hello'
    return msg

# 함수 호출
hello()
print(hello2())

add(1024, 5) 
sub(1024, 1000)
mul(512,2)
div(108,10)

