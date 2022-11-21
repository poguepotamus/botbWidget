from json import load, dump
from botb.settings import BOTB_DATA_FILE

def get_botb_data():
	with open(BOTB_DATA_FILE, 'r', encoding='utf-8') as data_file:
		return load(data_file)

def write_botb_owner_data(owner_data):
	botb_data = get_botb_data()
	botb_data['gifts'] = owner_data
	with open(BOTB_DATA_FILE, 'w', encoding='utf-8') as data_file:
		dump(botb_data, data_file, indent=4)