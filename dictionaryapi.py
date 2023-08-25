import requests

def get_definition(word):
	DICT_BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
	url = DICT_BASE_URL + word
	r = requests.get(url)
	if r.status_code != 200:
		#print(f"Failed to get definition for word {word}")
		return None

	body = r.json()
	if len(body) > 0 and 'meanings' in body[0] and len(body[0]['meanings'])>0 and \
	'definitions' in body[0]['meanings'][0] and len(body[0]['meanings'][0]['definitions'])>0 and \
	'definition' in body[0]['meanings'][0]['definitions'][0]:
		return body[0]['meanings'][0]['definitions'][0]['definition']
	else:
		#print(f"Definition not found for {word}")
		return None

