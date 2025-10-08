import numpy as np


def santas_instruction(array_light):
	#instruction 1
	array_light[887:960, 9:630] = 1
	#instruction 2
	array_light[454:845, 398:449] = 1
	#instruction 3
	array_light[539:560, 243:966] = 0
	#instrucion 4
	array_light[370:677, 819:869] = 0
	#instruction 5
	array_light[145:371, 40:998] = 0
	#instruction 6
	array_light[301:809, 3:454] = 0
	#instruction 7
	array_light[351:952, 678: 909] = 1
	#instruction 8
	array_light[720:898, 196:995] = (array_light[720:898, 196:995] + 1) % 2 #toggle
	#instruction 9
	array_light[831:905, 394:861] = (array_light[831:905, 394:861] + 1) % 2 #toggle

	return array_light

def news_santas_instruction(array_light):
	#instruction 1
	array_light[887:960, 9:630] += 1
	#instruction 2
	array_light[454:845, 398:449] += 1
	#instruction 3
	array_light[539:560, 243:966] = array_light[539:560, 243:966] - 1*(array_light[539:560, 243:966] != 0)
	#instrucion 4
	array_light[370:677, 819:869] = array_light[370:677, 819:869] - 1*(array_light[370:677, 819:869] != 0)
	#instruction 5
	array_light[145:371, 40:998] = array_light[145:371, 40:998] - 1*(array_light[145:371, 40:998] != 0)
	#instruction 6
	array_light[301:809, 3:454] = array_light[301:809, 3:454] - 1*(array_light[301:809, 3:454] != 0)
	#instruction 7
	array_light[351:952, 678: 909] += 1
	#instruction 8
	array_light[720:898, 196:995] += 2 #toggle
	#instruction 9
	array_light[831:905, 394:861] += 2 #toggle

	return array_light

lights = np.zeros((1000,1000))
print(santas_instruction(lights).sum())
lights2 = np.zeros((1000,1000))
print(news_santas_instruction(lights2).sum())

