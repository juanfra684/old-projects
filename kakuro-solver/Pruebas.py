# posibles = [ [1,2] , [9] ]

# dom = [1,2,3,4,5,6,7,8,9]

# j = 0
# k = 0

# while (j < len(posibles)):
# 	while (k < len(posibles[j])):
# 		if (posibles[j][k] in dom):
# 			dom.remove(posibles[j][k])
# 			k += 1
# 		else:
# 			k += 1
# 	print "voy a aumentar a j"
# 	j += 1
# 	k = 0

# print dom


def prueba(dato):
	if dato == "#":
		return "#"
	else:
		return dato

print prueba(8)