import ipaddress
# Example of valid IPv6 address
print (ipaddress.ip_address(u'2001:0db8:85a3:2bfe:070d:8a2e:0370:7334'))
    
# Invalid IPv6 address raises error
print (ipaddress.ip_address(u'2001:0db8:85a3:0ff0:00000:8a2e:0370:7334'))
