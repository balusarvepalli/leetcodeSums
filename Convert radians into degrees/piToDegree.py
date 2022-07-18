import math
def degree_converter(x):
    x = float(input("Enter your value in radian: "))
    print(x)
    pi_value=math.pi
    degree=(x*180)/pi_value
    return degree
print("The degree of the given radian is :",degree_converter('x'))