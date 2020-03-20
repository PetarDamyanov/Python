def gas_stations(distance, tank_size, stations):
    stations_stops=[]
    first=stations[0]
    for x in stations:
    	if x<=tank_size:
    		if first<=x:
    			first=x
    s_next=first
    s_prev=first
    stations_stops.append(first)
    while s_next<=distance:
    	s_next=s_next+tank_size
    	for x in stations:
    		if x<s_next:
    			if s_prev<x:
    				s_prev=x
    	#print(s_next)
    	stations_stops.append(s_prev)
    
    





    print(stations_stops)






gas_stations(320, 90, [50, 80, 140, 180, 220, 290])

gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])

