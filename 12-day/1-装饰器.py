def w1(fun):
	def inner():
		print("验证")
		fun()
	return inner

def test():
	print("哈哈哈")


#f = w1(test)
#f()

test = w1(test)
test()