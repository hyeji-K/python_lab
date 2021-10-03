# 비교 연산
x = 10
y = 12
print('x > y is', x>y)
print('x < y is', x<y)
print('x == y is', x==y)
print('x != y is', x != y)
print('x >= y is', x >= y)
print('x <= y is', x <= y)

# 논리 연산
xx = True
yy = False
print('xx and yy id', xx and yy)
print('xx or yy is', xx or yy)
print('not xx is', not xx)

# 식별 연산
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]
# 리터럴의 속성상 리스트 둘은 다름. 논리연산으로는 참 
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)