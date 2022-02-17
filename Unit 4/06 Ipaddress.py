import ipaddress

# IPv4 address
print(type(ipaddress.ip_address(u'175.198.42.211')))
print(type(ipaddress.ip_address(u'5.0.0.1')))

# IPv6 address
print(type(ipaddress.ip_address(u'2001:0db8:85a3:2bfe:070d:8a2e:0370:7334')))
print(type(ipaddress.ip_address(u'0000:f0f0::7b8a:ffff')))
