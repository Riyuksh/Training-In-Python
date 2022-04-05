import math
x0 = int(input('Enter X-axis : '))
y0 = int(input('Enter Y-axis: '))
gravity = 9.8
angle = int(input('Enter degree (0-90): '))     
velocity = int(input('Enter velocity: '))  
Cosine = math.cos(math.degrees(angle))
Sine = math.sin(math.degrees(angle))
Tangent =  Sine/Cosine

print("The trajectory would be :  ")

Value = x0*Tangent - (gravity*x0*x0)/(2*velocity*velocity*Cosine*Cosine) + y0
print(Value)