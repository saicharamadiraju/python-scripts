class Person:
	def __init__(saicharan, name, age):
		saicharan.name = name
		saicharan.age = age
	def myfun(s1):
		print("Hello My name is " +s1.name)
		print ("My age is " +str(s1.age))
p1 = Person("sai",29)
p1.myfun()