
class Image:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.pixels = [[None for x in range(width)] for y in range(height)]

	def set_pixel(self, x, y, col):
		self.pixels[y][x] = col

	def write_ppm(self, img_file):

		def to_byte(c):
			return round(max(min(c * 255, 255), 0))

		ppm_header = f"P3 {self.width} {self.height}\n255\n"

		ppm_data = ""
		for row in self.pixels:
			for color in row:
				ppm_data += "{} {} {} ".format(
					to_byte(color.x), to_byte(color.y), to_byte(color.z))
			ppm_data += "\n"

		ppm_content = ppm_header + ppm_data
		img_file.write(ppm_content)
