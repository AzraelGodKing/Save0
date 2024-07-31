clear()
while True:
	start = 0
	worldsize = get_world_size()
	ground = get_ground_type()
	while start < worldsize:
		for i in range(worldsize):
			if num_items(Items.hay) < 100000:
				hay()
				move(North)
			elif num_items(Items.Wood) < 100000:
				wood()
				move(North)
			elif num_items(Items.Carrot) < 100000:
				carrots()
				move(North)
			elif num_items(Items.Pumpkin) < 100000:
				pumpkins()
				move(North)
		move(East)