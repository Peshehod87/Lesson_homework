with open ('referat.txt', 'r', encoding = 'utf-8') as f:
	line = f.read().lower()
	print (len(line))
	n=0
	for i in line:
		i = line.split()
		if i == ' ':
			k -=1
		elif i =='с':
			k -=1
		elif i =='в':
			k -=1
		elif i =='на':
			k -=1
		elif i =='у':
			k -=1
		elif i =='то':
			k -=1
		elif i ==',':
			k -=1
		#print (i)
	print(n)
	print(k)

	'''for line in f:
		line = line.readlines()
		print(line)
		'''
	
	
