import math

class Vector:
	"""A three element vector used in 3D graphics for multiple purposes"""
	def __init__(self, x=0.0, y=0.0, z=0.0):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return ("{}, {}, {}".format(self.x, self.y, self.z))

	def magnitude(self):
		return math.sqrt(self.dot_product(self))

	def normalize(self):
		return self / self.magnitude()

	def dot_product(self, other):
		return self.x * other.x + self.y * other.y + self.z * other.z

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

	def __mul__(self, scaler):
		assert not isinstance(scaler, Vector)
		return Vector(self.x * scaler, self.y * scaler, self.z * scaler)

	def __rmul__(self, scaler):
		return self.__mul__(scaler)

	def __truediv__(self, scaler):
		assert not isinstance(scaler, Vector)
		return Vector(self.x / scaler, self.y / scaler, self.z / scaler)
