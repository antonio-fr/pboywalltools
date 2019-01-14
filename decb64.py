import base64

m1 = 'Y29uZHVpcmU='
m2 = 'dHJpb21waGU='

def dec( str ):
	return base64.decodestring(str)

print dec(m1)
print dec(m2)

