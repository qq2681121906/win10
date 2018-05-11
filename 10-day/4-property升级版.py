class LaoWang(object):

	def __init__(self):
		self.__money = 1000
	
	@property
	def money(self):
		return self.__money
	
	@money.setter
	def money(self,money):
		self.__money = money
	#money = property(getMoney,setMoney)	

laowang = LaoWang()
laowang.money = 100
print(laowang.money)