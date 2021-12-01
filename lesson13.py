from functools import wraps

def my_decorator(*args, **kwargs):
	def actually_decorator(func):
		def wrapper(*func_args, **func_kwargs):
			func(*func_args, **func_kwargs)
			print(*args)
		return wrapper
	return actually_decorator

def counter(func):
	@wraps(func)
	def wrapper(*args):
		wrapper.runs += 1
		func(*args)
		print('Succesfulr runs: {}'.format(wrapper.runs))
	wrapper.runs = 0
	return wrapper

def log(func):
	def wrapper(*args):
		res = func(*args)
		print(*args)
		print(res)
		return res
	return wrapper

def decorator1(func):
	def wrapper(*args):
		print('Decorator 1 before func')
		func(*args)
		print('Decorator 1 after func')
	return wrapper

def decorator2(func):
	def wrapper(*args):
		print('Decorator 2 before func')
		func(*args)
		print('Decorator 2 after func')
	return wrapper

#@decorator1
#@decorator2
@my_decorator('This is Spartaaaaaaa!')
def say_hello():
	print('Hello World')

say_hello()
say_hello()
say_hello()

#print(say_hello.__name__)

'''@counter
def dummy(*args):
	pass

@counter
@log
def sum_two_numbers(a, b):
	return a + b

#s = sum_two_numbers(6, 4)
#print(s)
#say_hello('World')

#print(say_hello.__name__)
#print(dummy.__name__)'''