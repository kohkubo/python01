def my_var():
	print('42 has a type', type(42))
	print('42 has a type', type('42'))
	print('forty-two has a type', type('forty-two'))
	print('42.0 has a type', type(42.0))
	print('True has a type', type(True))
	print('[42] has a type', type([42]))
	print("{'42': '42'} has a type", type({'42': '42'}))
	print('(42,) has a type', type((42,)))
	print('{42} has a type', type(set("42")))

if __name__ == '__main__':
	my_var()
