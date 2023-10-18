def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)

fact_input=int(input("Enter a number: "))
res=fact(fact_input)
print("The factorial of {} is {}".format(fact_input,res))