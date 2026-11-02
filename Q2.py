text=input("enter the string:")
vowels="aeiouAEIOU"

v_count=c_count=d_count=s_count=0
for char in text:
   if char.isalpha():
      if char in vowels:
         v_count+=1 
      else:
         c_count+=1
   elif char.isdigit():
       d_count+=1
   elif char.isspace():
       s_count+=1


#print("vowels:",v_count,int())
#print("consonant:",c_count,int())
#print("digit:",d_count,int())
#print("space:",s_count,int())

print(f"vowels:{v_count}")
print(f"consonant:{c_count}")
print(f"digit:{d_count}")
print(f"space:{s_count}")

#convert the strin into uppercase, lowercase, and title case.

text =input("enter a string:")
print("uppercase:", text.upper())
print("lowercase:",text.lower())
print("titlecase:",text.title())


#CHECK THE given input is anagrams

text1=input("enter the first string:")
text2=input("enter the second string:")

clean_text1=text1.replace(" ","").lower()
clean_text2=text2.replace(" ","").lower()

if sorted(clean_text1)==sorted(clean_text2):
   print("the strings are anagrams.")
else:
   print("the strings are not anagrams.")