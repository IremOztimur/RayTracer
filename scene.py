class Scene:
	"""Scene has all the information needed for the ray tracing engine"""
	def __init__(self, width, height, camera, lights, objects):
		self.width = width
		self.height = height
		self.camera = camera
		self.objects = objects
		self.lights = lights

