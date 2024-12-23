import re

version_pattern = re.compile(r'Cisco .+ Software, Version (\S+)')
model_pattern = re.compile(r'cisco (\S+).+bytes of memory\.')
serial_number_pattern = re.compile(r'Processor board ID (\S+)')
uptime_pattern = re.compile(r'(.+) uptime is (.*)')

with open('show_version.txt') as file:
    output = file.read()
    version_match = version_pattern.search(output)
    print(version_match)
    print(version_match.group(1))
    print('IOS Version:'.ljust(18) + version_match.group(1))
    model_match = model_pattern.search(output)
    print('Router model is:'.ljust(18) + model_match.group(1))
    serial_number_match = serial_number_pattern.search(output)
    print('Serial number is:'.ljust(18) + serial_number_match.group(1))
    uptime_match = uptime_pattern.search(output)
    print('Hostname is:'.ljust(18) + uptime_match.group(1))
    print('Device uptime is:'.ljust(18) + uptime_match.group(2))