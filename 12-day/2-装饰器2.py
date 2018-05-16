def w1(fun):
	def inner():
		print("验证")
		fun()
	return inner

#test = w1(test)

@w1
def test():
	print("哈哈哈")

test()