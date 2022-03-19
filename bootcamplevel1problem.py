def old_macdonald(name):
	#UPPERCASE THE FIRST AND FOURTH CHARACTER OF THE NAME
	first_letter = name[0]
	inbetween_letter = name[1:3]
	fourth_letter = name[3]
	rest_letter = name[4:]

	return first_letter.upper() + inbetween_letter + fourth_letter.upper() + rest_letter