def parity(x):
    result=0
    while(x!=0):
        result^=x&1
        x>>=1
    return result
n=int(input("Enter the number which is to be checked"))
print(parity(n))
