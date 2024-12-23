#Import Regular expression library
import re


with open('show_version.txt') as ver_data:
    ver_output = ver_data.read()


#my_pattern = r"Cisco"
# my_pattern = r"Cisco.+, Version (\d\S+)"
# re_output = re.search(my_pattern, ver_output)
# print(re_output)

# version_output = re_output.group(1)

# print(f"{'IOS Version:'.ljust(10)}: {version_output}")

# my_pattern = r"(cisco)\.(com)"
# re_output = re.search(my_pattern, ver_output)

# if re_output:
#     print("Match found")
#     print(re_output.group(0))
#     print(re_output.group(1))
#     print(re_output.group(2))

############################ RegEx Pattern object using re.compile()

''' compile '''

# my_pattern =  re.compile(r"(Cisco)\.(\w+)")
# result = my_pattern.search(string=ver_output)

#It will print only the first match
# print(result)

# #It will print all matches
# print(my_pattern.findall(string=ver_output))


''' compile example'''
my_pattern = re.compile(r"C....")
print(my_pattern.search(string=ver_output))
# #It will print all matches
# print(my_pattern.findall(string=ver_output))
# print(my_pattern.finditer(string=ver_output))

# results = my_pattern.finditer(string=ver_output)
# for result in results:
#     print(result)

''' Validate User Input'''

# input1 = input ("Enter Python version:")
# my_pattern = re.compile(r"python3|python3.10")
# match = my_pattern.search(input1)
# if match:
#     print(f"Matched with {input1}")
# else:
#     print("No match found")


''' E-mail validation pattern'''
support_email = 'Please send us mail to help@gmail.com, support@gmail.com, admin@gmail.co.in, abc@abc.co.uk, abc@aa.co.uk'
email_pattern = re.compile(r"[\w\.-]+@[\w\.-]+.co[m|\.](\w{2})?")
results = email_pattern.finditer(string=support_email)
for result in results:
    print(result.group())
