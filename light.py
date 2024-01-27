from color import Color

class Light:
	"""Light represents a point light source of a certain color"""
	def __init__(self, pos, color = Color.from_hex_to("#FFFFFF")):
		self.pos = pos
		self.color = color

