from color import Color

class Material:
	"""Material has color and properties which tells us how it reacts to light"""
	def __init__(self, base_color=Color.from_hex_to("#FFFFFF"), ambient=0.05, diffuse=0.5, specular=0.5):
		self.base_color = base_color
		self.ambient = ambient
		self.diffuse = diffuse
		self.specular = specular

	def color_at(self, position):
		return self.base_color
