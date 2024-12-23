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

my_pattern = r"(cisco)\.(com)"
re_output = re.search(my_pattern, ver_output)

if re_output:
    print("Match found")
    print(re_output.group(0))
    print(re_output.group(1))
    print(re_output.group(2))