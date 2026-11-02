
#check the name is python or not 
name =input("Enter the name to check:")
if name.isidentifier():
    print(f"'{name}'is a valid python identifier.")
else:
    print(f"'{name}' is not valid python identifier. ")

#print all python keywords


    import keyword
print("Python Keywords:")
print(keyword.kwlist)

#accept a variable name and check it is keyword
import keyword
var_name=input("enter the variable name:")
if keyword.iskeyword(var_name):
    print(f"'{var_name}' is a reserved python keyword.")
else:
    print(f"'{var_name}' is not a reserved python keyword.")

#wap to accept two integer and perform add, sub, multi, divi,modulus.
num1=int(input("enter the first integer:"))
num2=int(input("enter the second integer:"))
print(f"addition:{num1 + num2 }")
print(f"subtraction:{num1 - num2}")
print(f"multiplication:{num1*num2}")
print(f"division:{num1/num2}")
print(f"modulus(remainder):{num1%num2}")

#find the real and imaginary part of a complex number entered by the user.

comp_num= complex(input("enter a complex number:"))
print(f"real part : {comp_num.real}")
print(f"imaginary part:{comp_num.imag}")

#check number is odd or even using bool

num=int(input("enter the number:"))
is_odd=bool(num%2)
if is_odd:
    print(f"{num} is odd.")
else:
    print(f"{num} is even.")

    #wap to demonstreare the difference b/w (float division and //floor division ) using integer and floats.

    num=int(input("enter the number:"))
is_odd=bool(num%2)
if is_odd:
    print(f"{num} is odd.")
else:
    print(f"{num} is even.")

    #swap the two number without using third variable.

    a=float(input("enter value for a:"))
b=float(input("enter value for b:"))
a,b=b,a
print(f"after swapping: a={a},b={b}")

