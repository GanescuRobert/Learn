
class Journey:
	def __init__(self,*movement_list):
		self.travel= movement_list
	def is_round_trip(self):
		x_pos,y_pos=0,0
		for movement in self.travel:
			x_pos+=movement[0]
			y_pos+=movement[1]
		return x_pos==0 and y_pos==0
peter_itinerary = [[90,50],[-80,-40],[-10,-10]]
peter_journey = Journey (*peter_itinerary)
print(peter_journey.is_round_trip())

susan_itinerary = [[50,40],[-60,10],[20,-70],[10,30]]
susan_journey = Journey (*susan_itinerary)
print(susan_journey.is_round_trip())
