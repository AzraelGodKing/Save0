def carrots():
	if get_ground_type() != Grounds.Soil:
		till()
	else:
		if num_items(Items.Carrot_Seed) == 0:
			trade(Items.Carrot_Seed,16)
		else:
			if get_entity_type() == None:
				plant(Entities.Carrots)
			else:
				if can_harvest():
					harvest()
				
			
			
		
		
	