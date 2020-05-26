favorite_languages = {'jen': 'python', 'sarah': 'c','edward': 'ruby', 'phil': 'python',
'artemis':'not polled', 'joey':'not polled'}

for name in favorite_languages.keys():
	if 'not polled' != favorite_languages[name]:
		print(name.title() + ', thank you for taking the poll!')
	else:
		print(name.title() + ', please take the poll!')