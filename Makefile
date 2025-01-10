clean:
	@rm -rf __pycache__
	@rm -rf srcs/__pycache__
	@rm -rf *.ppm
	@echo "\033[91mCleaned up __pycache__\033[0m"
	@echo "\033[91mCleaned up *.ppm\033[0m"


open:
	@open *.ppm
	@echo "\033[92mOpening *.ppm files\033[0m"

run:
	@python3 srcs/main.py
	@echo "\033[92mRunning main.py\033[0m"