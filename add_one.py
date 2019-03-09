Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #File: add_one.py

>>> def add_one(number):
	number_string = str(number)
	digits = list(number_string)
	digits2 = [str(int(i)+1) for i in digits]
	final_number = "".join(digits2)
	return int(final_number)


>>>python -i script.py
