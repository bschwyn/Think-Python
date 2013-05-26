#2
#In Robert McCloskey's book Make Way for Ducklings, the namees of the ducklings are Jack, Kack, Lack,
# Mack, Nack, Ouack, Pack, and Quack. This loop tries to output these names in order.

prefixes = "JKLMNOPQ"
suffix = "ack"

for cha in prefixes:
	if cha == 'O' or 'Q':
		print(cha+'u'+suffix)
	else:
		print(cha+suffix)
	
