
data = 6

if data < 0:
    print('This is negative number')
else:
    if data % 2 == 0:
        print('This is Even number')
    else:
        print('This is Odd number')

# 2 przykład

if data >= 0:
    if data % 2 == 0:
        print('This is Even number')
    else:
        print('This is Odd number')                                


# 3 przykład

if data >= 0 and data % 2 == 0:
    print('This is Positive  number')    
elif data >= 0 and data % 2 == 1:
    print('This is Negative number')          

# for
li = [43, 56, 34, 45, 77]
z = 0
for i in li:
    z = z+i

print(z)  # 255

# while
i = 1
z = 8

while i <=10:
    print(i * z)   
    i+=1    # 8*1, 8*2, 8*3, 8*4 --> do 10

i = 10
z = 8
while i >=1:
    print(i * z)
    i -= 1
    
print('')
print('-------------------')
i = 10
z = 8
while i >=1:
    print(i * z)
    i -= 2

# string
a = '   Hello'
b = 'Hello   '

if a.strip() == b.strip():
    print('Strimg are same') 
else:
    print('Not same')        

a = 'Hello'
b = 'HELLO'
if a.lower() == b.lower():
    print('Strimg are same') 
else:
    print('Not same')        

# funkcje
def multiply(a,b):
    c = a*b
    return c

def add(a,b):
    c = a+b
    print(c)

x = multiply(4,20)  #80
add(x, 10)          #90


        