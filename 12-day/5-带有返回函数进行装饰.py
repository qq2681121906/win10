def w1(fun):
	print("正在装饰")
	def inner():
		print("验证")
		ret = fun()
		return ret
	return inner

#test = w1(test)

@w1
def test():
	return "哈哈哈"
ret = test()
print(ret)