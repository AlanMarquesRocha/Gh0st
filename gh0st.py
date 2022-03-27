with open('gh0st.lst', 'w') as archive:
	# <code>
	import random
	import string
	
	count = 1E8
	i = 0
	
	def random_keys(size = 8, chars = string.ascii_lowercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))
	while i < count:
		print(random_keys(), file = archive)
		i = i + 1
