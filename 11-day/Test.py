def fid():
	i = 0
	a,b = 0,1
	while i < 8:
		#print(b)
		print("-----haha-----")
		yield b
		print("-----hehe-----")
		a,b = b,a+b
		i+=1
		
b = fid()
