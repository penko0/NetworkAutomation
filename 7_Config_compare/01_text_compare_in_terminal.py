import difflib

with open('golden_config.txt') as g_data:
    g_config = g_data.read()

with open('new_config.txt') as n_data:
    n_config = n_data.read()

#print(n_config)

delta = difflib.Differ().compare(g_config.splitlines(), n_config.splitlines())

print(delta)

for data in delta:
    print(data)