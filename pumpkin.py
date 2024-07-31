def pumpkins():
	if get_ground_type() != Grounds.Soil:
		till()
	else:
		if num_items(Items.Pumpkin_Seed) == 0:
			trade(Items.Pumpkin_Seed,16)
		else:
			if get_entity_type() == None:
				plant(Entities.Pumpkin)
			else:
				if can_harvest():
					harvest()
				
			