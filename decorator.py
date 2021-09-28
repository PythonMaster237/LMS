import time
def my_decorator(func):
	def wrapper(*args, **kwargs):
		try:
			func(*args, **kwargs)
			print('Done:', '\t', time.ctime())
			print('Name func:', '\t', func.__name__)
			print('Arguments:', '\t', *args, **kwargs)
		except RuntimeError as e:
			print(str(e))
	return wrapper

#@my_decorator
def my_func(num):
	if num%2:
		raise RuntimeError('Just for fun!')
	else:
		print(num)

def sum_two_numbers(a, b):
	print(a + b)

my_func = my_decorator(my_func)
sum_two_numbers = my_decorator(sum_two_numbers)
my_func(3)
sum_two_numbers(4, 5)