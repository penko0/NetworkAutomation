from genie.testbed import load
tb = load('yaml/my_testbed.yaml')
dev = tb.devices["CSR3"]
dev.connect()
show_version_parsed = dev.parse("show version")
print(show_version_parsed['version']['version_short'])