import re

default_route_pattern = re.compile(r'ip route 0.0.0.0 0.0.0.0.+?([\d\.]+)\n')
static_route_pattern = re.compile(r'ip route (?P<dst_subnet>[^0][\d\.]+) (?P<netmask>[^0][\d\.]+)')

with open('show_running-config.txt') as file:
    output = file.read()

default_route_match = default_route_pattern.search(output)
if default_route_match:
    print('\n' + 'Default Gateway:'.ljust(18) + default_route_match.group(1))
else:
     print('\n' + 'Default Gateway:'.ljust(18) + 'Not Available')

static_route_match = static_route_pattern.finditer(output)
static_route_list = list()
for static_route in static_route_match:
    static_route_list.append(static_route.groupdict())
    #print(static_route.groupdict())
print("Here are the static routes configured:"'\n' + str(static_route_list))