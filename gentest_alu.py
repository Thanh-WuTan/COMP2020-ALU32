import random
import sys

sys.stdout = open('alu_test_vector.txt', 'w')

print("Op[4] A[32] B[32] Sa[5] C[32] V")

print('''
# Those logic operations, such as and, or, xor, nor, shifting, will use binary
# The others operations, including comparations, addition, and subtraction, will use decimal 
''')

print('#The following test cases are used to test AND operation')
#### AND ####
for tc in range(100):   
    a = ''
    b = ''
    c = ''
    for j in range(32):
        a_i = random.randint(0, 1)
        b_i = random.randint(0, 1)
        a+= str(a_i)
        b+= str(b_i)
        c+= str(a_i and b_i)
    op = "0100"
    v = 0
    s = 0
    print(op, a, b, s, c, v)

print('#The following test cases are used to test OR operation')
#### OR ####
for tc in range(100):
    a = ''
    b = ''
    c = ''
    for j in range(32):
        a_i = random.randint(0, 1)
        b_i = random.randint(0, 1)
        a+= str(a_i)
        b+= str(b_i)
        c+= str(a_i or b_i)
    op = "0101"
    v = 0
    s = 0
    print(op, a, b, s, c, v)

print('#The following test cases are used to test XOR operation')
#### XOR ####
for tc in range(100):
    a = ''
    b = ''
    c = ''
    for j in range(32):
        a_i = random.randint(0, 1)
        b_i = random.randint(0, 1)
        a+= str(a_i)
        b+= str(b_i)
        c+= str(a_i ^ b_i)
    op = "1010"
    v = 0
    s = 0
    print(op, a, b, s, c, v)


print('#The following test cases are used to test NOR operation')
#### NOR ####
for tc in range(100):
    a = ''
    b = ''
    c = ''
    for j in range(32):
        a_i = random.randint(0, 1)
        b_i = random.randint(0, 1)
        a+= str(a_i)
        b+= str(b_i)
        Or = str(a_i or b_i)
        c+= "1" if a_i == 0 and b_i == 0 else "0"
    op = "1011"
    v = 0
    s = 0
    print(op, a, b, s, c, v)


print('#The following test cases are used to test NE operation')
#### NE ####
for tc in range(100):
    a = random.randint(-2 ** 31 , 2 ** 31 - 1)
    b = random.randint(-2 ** 31, 2 ** 31 -1)
    tmp = random.random()
    if tmp <= 0.45:
        b = a
    if a == b:
        c = 0
    else:
        c = 1
    op = "1000"
    v = 0
    s = 0
    print(op, a, b, s, c, v)


print('#The following test cases are used to test EQ operation')
#### EQ ####
for tc in range(100):
    a = random.randint(-2 ** 31 , 2 ** 31 - 1)
    b = random.randint(-2 ** 31, 2 ** 31 -1)
    tmp = random.random()
    if tmp <= 0.45:
        b = a
    if a != b:
        c = 0
    else:
        c = 1
    op = "1001"
    v = 0
    s = 0
    print(op, a, b, s, c, v)

print('#The following test cases are used to test LE operation')
#### LE ####
for tc in range(100):
    a = random.randint(-2**31, 2**31-1)
    b = random.randint(-2**31, 2**31-1)
    tmp = random.random()
    op = "1110"
    v = 0
    s = 0
    c = 1 if a <= 0 else 0
    print(op, a, b, s, c, v)

print('#The following test cases are used to test GT operation')
#### GT ####
for tc in range(100):
    a = random.randint(-2**31, 2**31-1)
    b = random.randint(-2**31, 2**31-1)
    tmp = random.random()
    op = "1111"
    v = 0
    s = 0
    c = 1 if a > 0 else 0
    print(op, a, b, s, c, v)

print('#The following test cases are used to test subtraction operation')
#### SUBSTRACT ####
for tc in range(100):
    a = random.randint(-2**31, 2**31-1)
    b = random.randint(-2**31, 2**31-1)
    tmp = random.random()
    op = "011"
    if tmp <= 0.45:
        op+= "0"
    else:
        op+= "1"
    v = 0
    c = a - b
    if c >= 2**31:
        v = 1
        c = c - 2**32
    elif c < -2**31:
        v = 1
        c = c + 2**32
    s = 0
    print(op, a, b, s, c, v)

print('#The following test cases are used to test addition operation')
#### ADD ####
for tc in range(100):
    a = random.randint(-2**31, 2**31-1)
    b = random.randint(-2**31, 2**31-1)
    tmp = random.random()
    op = "001"
    if tmp <= 0.45:
        op+= "0"
    else:
        op+= "1"
    v = 0
    c = a + b  
    if c >= 2**31:
        v = 1
        c = c - 2**32
    elif c < -2**31:
        v = 1
        c = c + 2**32
    s = 0
    print(op, a, b, s, c, v)

print('#Random cases to test left shift operation')
#### left shift ####
for tc in range(100):
    op = "000" + str(random.randint(0, 1))
    a = 0
    s = random.randint(0, 31)
    v = 0
    b = ""
    c = ""  
    for j in range(32):
        b+= str(random.randint(0, 1))
    for j in range(32):
        if j + s < 32:
            c+= b[j + s]
        else:
            c+= '0'
    print(op, a, b, s, c, v)

print('#Random cases to test right shift logical operation')
#### right shift logical ####
for tc in range(100):
    op = "1100"
    a = 0
    s = random.randint(0, 31)
    v = 0
    b = ""
    c = ""  
    for j in range(32):
        b+= str(random.randint(0, 1))
    for j in range(32):
        if j - s >= 0:
            c+= b[j - s]
        else:
            c+= '0'
    print(op, a, b, s, c, v)

print('#Random cases to test right shift arithmetic operation')
#### right shift arth ####
for tc in range(100):
    op = "1101"
    a = 0
    s = random.randint(0, 31)
    v = 0
    b = ""
    c = ""  
    for j in range(32):
        b+= str(random.randint(0, 1))
    for j in range(32):
        if j - s >= 0:
            c+= b[j - s]
        else:
            c+= b[0]
    print(op, a, b, s, c, v)