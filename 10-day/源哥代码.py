#商店的基类(抽象类) 规定好商店要干的事情
#预订
#创建
class Store(object):

	def createFactory(self,type):
		pass

	def order(self,type):
		return self.createFactory(type)

class BmwStore(Store):

	def createFactory(self,type):
		return BmwFactory().selectCar(type)


class BCStore(Store):
	def createFactory(self,type):
		return BCFactory().selectCar(type)

class Factory(object):

	def selectCar(self,type):
		pass

class BCFactory(Factory):
	
	def selectCar(self,type):
		if type == 0:
			return Bmw730()
		elif type == 1:
			return Bmwx5()	

		
class BmwFactory(Factory):
	
	def selectCar(self,type):
		if type == 0:
			return DaG()
		elif type == 1:
			return XiaoG()			

class Car(object):
	def move(self):
		print("在移动")

	def music(self):
		print("播放音乐")	


class Bmw730(Car):
	pass


class Bmwx5(Car):
	pass


class DaG(Car):
	pass

class XiaoG(Car):
	pass	

if __name__ == '__main__':
	store = BmwStore()
	bmwx5 = store.order(1)
	bmwx5.move()
	bmwx5.music()	
	