class LaoWang(object):

	def __init__(self):
		self.__money = 1000

	def setMoney(self,money):
		self.__money = money

	def getMoney(self):
		return self.__money

	money = property(getMoney,setMoney)	

laowang = LaoWang()
laowang.setMoney(100)
print(laowang.getMoney())

laowang.money = 100
print(laowang.money)