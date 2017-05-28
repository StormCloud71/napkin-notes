import random
def fun1(x,y):
    return (x+y)

def fun2(x,y):
    return (x*y)

def fun3(x,y):
    return (x**y)

class MultiCulti:
	def __init__(self):
		self.fundic={1:fun1,2:fun2,3:fun3}
	def result(self,pickfun=2,x=1,y=1):
		if pickfun not in self.fundic:
			return "Skata!"
		else:
			return self.fundic[pickfun](x,y)
	def try_luck(self):
		return(self.result(pickfun=(random.choice([1,2,3]))))

a=MultiCulti()
print a.result(4)
print a.try_luck()
