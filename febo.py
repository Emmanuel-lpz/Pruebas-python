#secuencia febonacci

def febonacci(n ):
    a = 0
    b = 1

    for i in range(n):
        c = a+b
        a = b
        b = c
    return b

for x in range (10):
     print(febonacci(x))

#def fibo(max):
#    a = 0
#    b = 1
##    while a < max:
 #      a = b
  #      b = a+b



