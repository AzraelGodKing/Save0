clear()
while True:
	start = 0
	worldsize = get_world_size()
	while start < worldsize:
		for i in range(worldsize):
			planted=get_entity_type()
			if planted==None:				
				plant(Entities.Bush)
			if can_harvest():
				harvest()				
				plant(Entities.Bush)
			move(North)
		move(East)
		start = start+1