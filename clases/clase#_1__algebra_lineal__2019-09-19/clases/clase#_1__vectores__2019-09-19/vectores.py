import math
class vectors():
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def in_one_vector(self):
		self.Vec=[self.x,self.y]
	def module(self,x0,y0):
		self.x0=x0
		self.y0=y0
		self.X=(self.Vec[0]-self.x0)**2
		self.Y=(self.Vec[1]-self.y0)**2
		print(self.X,"X")
		print(self.Y,"Y")		
		Module=math.sqrt(self.Y+self.X)
		return Module		
	def direccion(self):
		angle=math.degrees(math.atan((self.y/self.x)))
		return angle
	def sum(self,x0,y0):
		self.x0=x0
		self.y0=y0
		X0=self.Vec[0]+self.x0
		Y0=self.Vec[1]+self.y0
		V=[X0,Y0]
		return V
	def inner_product(self,angle2):
		self.angle2=angle2
		print(self.angle2)
		if self.angle2<=180 and self.angle2>=0:
			self.product_scalar=self.X*self.Y*math.cos(math.radians(self.angle2))
			print(math.cos(math.radians(self.angle2)))
			print(self.X,"X")
			print(self.Y,"Y")	
			return self.product_scalar
	def transposed(self,matriz):
		self.matriz=matriz
		if type(matriz):
			self.reverse=[i for i in reversed(self.matriz)]
			print(self.reverse,len(matriz))

V=vectors(4,8)
V.in_one_vector()
print(V.module(10,11))
print(V.direccion())
print(V.sum(1,1))
print(V.inner_product(60))
V.transposed([[[4],[5],[6]],[[4],[5],[6]]])