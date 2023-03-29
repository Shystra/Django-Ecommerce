def foo(n):
    if n >1:
        return n * foo (n-1)
    return n 
print(foo(4))




def contador (* num):
    tam = len (num)
    print (f'Recebi os valores {num} e sao ao todo {tam}')

contador (2,1, 3)

def somatoria (a,b):
    teste = a + b
    print(teste)
    

somatoria (2,3)
