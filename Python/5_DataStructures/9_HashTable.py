class HashTable(object):
	def __init__(self):
		self.array = [0 * 10]

	def hashFunction(self, key):
		return hash(key) % 10  # hash function only in python, not in JS

	def get(self, key):
		index = self.hashFunction(key)
		partition = self.array[index]
		if not partition: return False

		for _key, _val in partition:
			if _key == key:
				return _val



	def set(self, key, value):
		index = self.hashFunction(key)
		partition = self.array[index]

		if not partition: self.array[index] = [(key, value)]
		else: self.array[index].append((key, value))

		return True


	def getKeys(self):
		keys = []
		for i in self.array:
			if i != 0:
				for k, v in i:
					if k not in keys: keys.append(k)
		return keys



	def getValues(self):
		values = []
		for i in self.array:
			if i != 0:
				for k, v in i:
					if v not in values: values.append(v)
		return values
	
