# Basic
for i in range(151):
    print(i)

# Multiplos 5
print("======= multiplos de 5 =======")
for i in range(5,1001):
    if i % 5 == 0:
        print(i)

# Contar Dojo
print("======= contar dojo =======")
for i in range(0,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Whoa. Es un gran idiota
print("======= Whoa =======")
impares = []
for i in range(int(5e5)+1):
    if i % 2 != 0:
        impares.append(i)
print(f"suma es {sum(impares)}")

# cuenta regresiva a 4
print("======= Menos 4 =======")
for i in range(2018,-1,-4):
    print(i)

# flexible
print("======= Flexible =======")
low_num = 2
high_num = 19
mult = 5
for i in range(low_num, high_num+1):
    if i % mult == 0:
        print(i)
