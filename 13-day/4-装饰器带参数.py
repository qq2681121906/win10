def w2(p):
	def w1(fun):
		def inner(*args,**kwargs):
			if p == "hehe":
				print("-----验证-----")
			elif p == "haha":
				print("验证哈哈哈")
			ret = fun(*args,**kwargs)
			return ret
		return inner
	return w1


@w2("hehe")
def test(a,b):
	print("a==%d b==%d"%(a,b))
	return "hehehehe"

@w2("haha")
def test1():
	print("哈哈哈")

@w2("laowang")
def test2(a,b):
	print("呵呵呵")

@w2("xiaoming")
def test3():
	return "嘎嘎嘎"

test1()
test2(1,2)
print(test3())
print(test(1,2))