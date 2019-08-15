from wwbox.action_helper import *

#action: Role|Ngt/Atk/Dth

#action: Classic | Ngt

action([],[
	saveplayer(player("poll",pd(
							player('''-insert target-'''),
							"Please select a Player to ...",
							player("self") ))),
	addeffect(player,"effectname",'''-value-''')
])


#action: Classic | Atk

action([],[])

	#action: ... save for ww
	
	action([
		condition(effect(player("self"),"save_for"),has,"ww")
	],[
		append_to_effect(player("self"),"attacked_by","ww","false")
	])
	
	#action: ... still attacked_by
	
	action([
		condition(effect(player("self"),"attacked_by"),not_has,"ww"),
		condition(effect(player("self"),"attacked_by"),not_has,"hexe") #TODO implementation of not_has
	],[
		setstatus #TODO implementation
	])


#action: Classic | Dth

action([],[])

	#action: ... kill nutte
	
	action([
		condition(effect(player("self"),"nutte_da"),"=",true)
	],[
		directkill(player("role","nutte"))
	])

		
#action: