class Engine(object):
	
	def __init__(self, mapa):
		self.mapa = mapa

	def play(self):

		current = self.mapa.opening.enter()
		previous_room


		pass

class Map(object):

	rooms = {"cozinha": Cozinha(),
			 "outside": Out(),
			 "casadebanho": CasaDeBanho(),
			 "corredor": Corredor(),
			 "saladeestar": Sala(),
			 "quarto": Quarto(),
			 "previous_room": None
			}

	def __init__(self, opening):
		self.opening = opening

	def set_previous(self, previous):
		self.rooms["previous_room"] = previous
		
	def previous(self):
		return self.rooms["previous_room"]


class Room(object):
	
	def enter(self):

		print "This is an undefined room"
		return "previous_room"


class Out(Room):
	def enter(self):
		print "You are outside. Go in?"
		ans = raw_input("> ")

		if "y" in ans.lowercase():
			return "cozinha"
		else:
			return "outside"


class Cozinha(Room):

	def enter(self):
		print "You are in the kitchen. Go to the corridor or outside?"
		ans = raw_input("> ")

		if "corr" in ans.lowercase():
			return "corredor"
		if "out" in ans.lowercase():
			return "outside"
		else:
			return "cozinha"

class CasaDeBanho(Room):
	pass

class Corredor(Room):
	def enter(self):
		print "You are in the corridor. Go to the kitchen, living room, bathroom, or the room?"
		ans = raw_input("> ")

		if "kitch" in ans.lowercase():
			return "cozinha"
		elif "bathr" in ans.lowercase():
			return "casadebanho"
		elif "room" == ans.lowercase():
			return "quarto"
		elif "livin" in ans.lowercase():
			return "saladeestar"
		else:
			return "cozinha"

class Quarto(Room):
	pass

class Sala(Room):
	pass