from vector import Vector

class Color(Vector):
	"""Stores color as RGB triplets. An alias for Vector"""
	@classmethod
	def from_hex_to(cls, hex_color="#000000"):
		x = int(hex_color[1:3], 16) / 255.0
		y = int(hex_color[3:5], 16) / 255.0
		z = int(hex_color[5:7], 16) / 255.0
		return cls(x, y, z)

