import re
# string = "abc"
# pattern = "ab*c"
# if re.match(pattern, string):
#     print('Match found')
# else:
#     print('No Match found')

# # 2. Plus Metacharacter
# string = "abc"
# pattern = r"ab+c"
# if re.match(pattern, string):
#     print('Match found')
# else:
#     print('No Match found')

# # 3. Curly Braces Metacharacter 
# string = "abbc"
# pattern = r"ab{2,}c"
# if re.match(pattern, string):
#     print('Match found')
# else:
#     print('No Match found')

# # 4. The wildcard metacharacter Notation:(.)
# string = "acab"
# pattern = r"a.b"
# if re.match(pattern, string):
#     print('Match found')
# else:
#     print('No Match found')

# # 5. Optional Metacharacter 
# string = "bc"
# pattern = r"a?bc"
# if re.match(pattern, string):
#     print('Match found')
# else:
#     print('No Match found')

# # 6. Caret Metacharacter
# string = "91878988898"
# pattern = r"^91"
# if re.match(pattern, string):
#     print('Match found')
# else:
#     print('No Match found')

# # 7. Character Metacharacter
# string = "aaabbbBABABA"
# pattern = r"[a-zA-Z]"
# if re.match(pattern, string):
#     print('Match found')
# else:
#     print('No Match found')

# # 8. Find all and character class
# text = "The cat and the dog sat on the mat"
# pattern =r"[abc]"
# matches = re.findall(pattern, text)
# print(matches)

# # 9. Shorthand for Numeric Characters
# text = "The meeting is scheduled at 9 AM"
# pattern =r"\D"
# matches = re.findall(pattern, text)
# print(matches)

# # 10. W shorthand
# text = "The sentence includes punctuations! \n"
# pattern =r"\W"
# matches = re.findall(pattern, text)
# print(matches)

# # 11. s/s shorthand
# text = "The sentence \t includes punctuations! \n"
# pattern =r"\S+"
# matches = re.findall(pattern, text)
# print(matches)

# # 12. Combining Shorthand & Metacharacters
# text = "Helloooo, Python is awesomeeeee!"
# pattern =r"\w*o+\w*"
# # \w* Matches zero or more alphanumeric characters
# # o+ : Matches one or more occurences of the letter 'o'
# # \w+ : Matches zero or more alphanumeric characters
# matches = re.findall(pattern, text)
# print(matches)

# #  13. Matching phone numbers
# text = "Please contact me at +1 (123) 456-7890 or via email at doe@example.com "
# # +1 (123) 456-7890
# pattern =r"\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?\d{1,4}"

# matches = re.findall(pattern, text)
# print(matches)

# # 14. Matching Emails
# text = "Please contact me at +1 (123) 456-7890 or via email at doe@example.com "
# # doe@example.com
# pattern =r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

# matches = re.findall(pattern, text)
# print(matches)

# # 14. Checking Validity of Emails
# text = "Please contact me at +1 (123) 456-7890 or via email at doe@example.com "
# # doe@example.com
# pattern =r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
# email = input("Enter email address:")
# matches = re.findall(pattern, text)
# if re.match(pattern,email):
#     print("Valid email")
# else:
#     print("Invalid email")

# 15. Matching Dates
text = "Date: 2023-06-08  1990-01-01"
pattern =r"\d{4}-\d{2}-\d{2}"
dates = re.findall(pattern, text)
print(dates)



