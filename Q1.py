text=input("enter a string:")
reversed_text=text[::-1]
print(reversed_text)

length = len(text)
print("length of the string :", length)

if text.lower()==reversed_text.lower():
    print("the string is polindrome.")

else:
    print("the string is not polindrome.")

