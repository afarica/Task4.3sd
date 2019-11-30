class ContactList(list):
	def search_by_name(self):
		all_contacts={'Avtandil':0500120801,
		'Shamir':0702010203,
		'Mary':0705678990,
		'Adilet':0704040205,
		'Nazik':0700345678}
		name=input('Enter the name:')
		print(all_contacts.get(name))

all_contacts=ContactList()
all_contacts.search_by_name()
