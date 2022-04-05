import math
A =  int(input('Enter Initial Amount: '))
P =  float(input('Enter Interest Rate: '))
n =  int(input('Enter Number of years: '))

Interest = A * pow((1 + P/100),n)

print("The Inerest Rate of  : ")
print(Interest)