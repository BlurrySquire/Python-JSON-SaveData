# created by https://github.com/BlurrySquire
# github repo: https://github.com/BlurrySquire/Python-JSON-SaveData/
# please do not advertise this as your own

import json, os

default_save = {
	"user_info": {
		"username": "guest_user"
	},
	"wins": 0,
	"loses": 0
}

save_name = 'save.json'

def set_default_save(value=default_save):
	default_save = value

def create_save(name='save', value=default_save, indent=4):
	global save_name
	save_name = f'{name}.json'

	with open(f'{name}.json', 'w') as f:
		f.write(json.dumps(value, indent=indent))

def reset_save():
	if os.path.exists(save_name):
		with open(save_name, 'w') as f:
			f.write(json.dumps(default_save))
		return read_save()

def read_save():
	if os.path.exists(save_name):
		with open(save_name, 'r') as f:
			return json.loads(f.read())
	else:
		return default_save

def write_save(save_value=default_save, indent=4):
	if os.path.exists(save_name):
		with open(save_name, 'w') as f:
			f.write(json.dumps(save_value, indent=indent))
