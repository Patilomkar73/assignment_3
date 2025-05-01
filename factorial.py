
num=int(input("Enter the number: "))

def factorial_(num):
    result=1
    for i in range(2,num+1):
        result*= i
    return result
    

sum=factorial_(num)
print(f"Factorial of {num} is {sum}")