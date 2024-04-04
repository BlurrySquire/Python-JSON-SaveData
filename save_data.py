# Licensed under MIT License as of April 2024
# Created by https://github.com/BlurrySquire
# Repo can be found at: https://github.com/BlurrySquire/Python-JSON-SaveData

import json
import os

class SaveFile:
	def __init__(self, filename: str) -> None:
		self.filename: str = filename
		self.already_existed = False

		# If the file doesn't exist, make it.
		if not os.path.exists(self.filename):
			open(self.filename, 'w').close()
			self.already_existed = True

	def read(self) -> dict:
		with open(self.filename, 'r') as file:
			return json.load(file)
	
	def write(self, contents: dict) -> None:
		with open(self.filename, 'w') as file:
			json.dump(contents, file)