class Component:
	"""Abstract class"""

	def __init__(self,*args, **kwargs):
		pass

	def component_function(self):
		pass

class Child(Component):
	"""docstring for Child"""
	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		#This is where we store the name of your child item!
		self.name = args[0]

	def component_function(self):
		print "{}".format(self.name)

class Composite(Component): # Inherits from the abstract class , Component

	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)
		
		self.name = args[0]

		self.children = []

	def append_child(self, child):
		self.children.append(child)

	def remove_child(self, child):
		self.children.remove(child)

	def component_function(self):
		print "{}".format(self.name)

		for i in self.children:
			i.component_function()


sub1 = Composite("submenu1")

sub11 = Child("sub_submenu 11")

sub12 = Child("sub_submenu 12")

sub1.append_child(sub11) 

sub1.append_child(sub12)

top = Composite("top_menu")

sub2 = Child( "submenu2")

top.append_child(sub1)
top.append_child(sub2)

top.component_function()

"""
top_menu
	submenu1
		sub_submenu 11
		sub_submenu 12
	submenu2
"""

