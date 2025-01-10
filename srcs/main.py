from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from image import Image
from light import Light
from material import Material

def main():
	WIDTH = 320
	HEIGHT = 200

	camera = Vector(0 ,0 ,-1)
	lights = [Light(Point(1.5, -0.5, -10.0), Color.from_hex_to("#FFFFFF"))]
	material = Material(Color.from_hex_to("#FF0000"), ambient=0.2)
	objects = [Sphere(Point(0,0,0), 0.5, material)]
	scene = Scene(WIDTH, HEIGHT, camera, lights, objects)
	engine = RenderEngine()
	img = engine.render(scene)

	with open("out.ppm", "w") as ppm_file:
		img.write_ppm(ppm_file)

if __name__ == '__main__':
	main()
