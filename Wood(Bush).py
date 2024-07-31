def wood():
	if (get_entity_type() != Entities.Bush):
		plant(Entities.Bush)
	else:
		if can_harvest():
			harvest()
			plant(Entities.Bush)