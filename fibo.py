def fibo(num):
    if(num == 0) or (num == 1):
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)

n = int(input("Digite um número: "))
print(fibo(n))

resdiv100 = fibo(n) % 100

print(resdiv100)



