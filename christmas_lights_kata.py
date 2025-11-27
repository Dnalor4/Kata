#première compréhension des instruction de santa
def instruction(list_l, instruction, map_points = (0,0,0,0)):
	if instruction == 'on':
		for i in range(map_points[0], map_points[2]+1):
			for j in range(map_points[1], map_points[3]+1):
				list_l[i][j] = True

	elif instruction == 'off':
		for i in range(map_points[0], map_points[2]+1):
			for j in range(map_points[1], map_points[3]+1):
				list_l[i][j] = False
	elif instruction == 'toggle':
		for i in range(map_points[0], map_points[2]+1):
			for j in range(map_points[1], map_points[3]+1):
				list_l[i][j] = not list_l[i][j]

	else :
		print('error')	
	return list_l

#seconde compréhension des instrucion de santa
def instruction2(list_l, instruction, map_points = (0,0,0,0)):
	if instruction == 'on':
		for i in range(map_points[0], map_points[2]+1):
			for j in range(map_points[1], map_points[3]+1):
				list_l[i][j] += 1

	elif instruction == 'off':
		for i in range(map_points[0], map_points[2]+1):
			for j in range(map_points[1], map_points[3]+1):
				if list_l[i][j] != 0:
					list_l[i][j] -= 1
	elif instruction == 'toggle':
		for i in range(map_points[0], map_points[2]+1):
			for j in range(map_points[1], map_points[3]+1):
				list_l[i][j] += 2

	else :
		print('error')	
	return list_l

#réalise les instuction demander par Santa  sur les plage demander:
#dans le premier type d'instruction :'on' True, 'off' False, 'toggle' inverse l'état
#dans le second type d'instruction :'on' +1, 'off' -1 (minimum 0), 'toggle' +2
def santas_instruction(list_l , instruction_demander):
	list_l = instruction_demander(list_l,'on',(887,9,959,629))
	list_l = instruction_demander(list_l,'on',(454,398,844,448))
	list_l = instruction_demander(list_l,'off',(539,243,559,965))
	list_l = instruction_demander(list_l,'off',(370,819,676,868))
	list_l = instruction_demander(list_l,'off',(145,40,370,997))
	list_l = instruction_demander(list_l,'off',(301,3,808,453))
	list_l = instruction_demander(list_l,'on',(351,678,951,908))
	list_l = instruction_demander(list_l,'toggle',(720,196,897,994))
	list_l = instruction_demander(list_l,'toggle',(831,394,904,860))
	return list_l

#Fait la somme des éléments d'une liste de dimension 2
def somme(list_l):
	s = 0
	for i in range(len(list_l)):
		for j in range(len(list_l)):
			s += list_l[i][j]

	return s

lights1 = santas_instruction([[False for _ in range(1000)] for _ in range(1000)],instruction)
lights2 = santas_instruction([[0 for _ in range(1000)] for _ in range(1000)],instruction2)
summ = somme(lights1)  
summ2 = somme(lights2)
print(summ)
print(summ2)


