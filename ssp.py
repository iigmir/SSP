print ("SS ability punishment check")
print ("SS may acyorm of 'Series Script' or 'Script Style'.")

#s1 is biggest amd s3 is smallest.

def ssp(s1,s2,s3,mag):
	print ("Ability are:")
	print ("s1:%s, s2:%s, s3:%s" %(s1,s2,s3))
	print ("Ability from diretor:",mag)
	print ("(s1+s2+s3)-(((s1-s3))*3)+diretor*0.2")
	print ("So we account the score like this:")
	if ((s1+s2+s3)-(((s1-s3))*3)+mag*0.2) > 0:
		return (s1+s2+s3)-(((s1-s3))*3)+mag*0.2
	else:
		print ("Warning! Punishment is at or under zero!")
		return 0
