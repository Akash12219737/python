# Write a program to print multiplicaton table of a given number using for loop
num  = int(input("Enter the number: "))
for i  in range(1, 11):
    # print(str(num) + " x " + str(i) + " = " + str(i*num) )
    print(f"{num} X {i} = {num*i}")


# Write a program to greet all the person names stored in alist l1 and which startwith 5
l1 = ["Akash", "Sam", "Sachin", "Ravi"]
for name in l1:
    if name.startswith("S"):
        print("Hello " + name)

    
# Write a program to print multiplicaton table of a given number using while loop
num = int(input("Enter the number: "))
i=1
while i <=10:
    print(f"{num} X {i} = {num*i}")
    i+=1
    
# Writa a program is given number is prime or not
num = int(input("Enter the number: "))
if num == 1:
    print("the number is not prime")
if num > 1:
   
   for i in range (2, num):
       if(num%i ==0):
           print("This is not prime")
           break
       else:
           print("This number is prime")
           
           
# Write a program to find the sum of first n natural nnumbers using while loop
num  = int (input("Enter the number: "))
i= 0
j= 1
while(j<=num):
    i = i+j
    j = j+1
print("Sum of the first", i)
  
  
  
# Write a program to calculate the factorial of a given number using for loop
num =int(input("Enter the number: "))
factorial = 1
while(num>1):
     factorial = factorial*num
     num =num-1
print("Factorial",factorial)        

#@@@@@using for loop @@@@@@@
num =int(input("Enter the number: "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print("factorial", fact)    
    