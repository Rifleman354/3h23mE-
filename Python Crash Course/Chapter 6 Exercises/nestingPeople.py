people = {'Helios':{'rank':'Archmagos', 'homeworld':'Uldan','age':'1800'},
'Belsarius Cawl':{'rank':'Archmagos', 'homeworld':'Mars', 'age':'10000'},
'Varnak':{'rank':'Magos','homeworld':'Tyran','age':'800'}}

for username, user_info in people.items():
	print('\nName: ' + username)
	rank = user_info['rank'] + ' of ' + user_info['homeworld']
	age = user_info['age']
	print(rank.title())
	print(age)