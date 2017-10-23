

def word_in_blank(word, blanks_in_text):
	"""looks for presence of specific blanks within the given paragraphs"""
	for n in blanks_in_text:
		if n in word:
			return n
	return None

def check_answer(user_guess,answer_list,word_position):
	if user_guess == answer_list[word_position]:
		print "Correct!\n"
		return True
		#return user_guess
	else:
		print "Incorrecto!"
		return False

def play_game(game_string, blanks_in_text, answers):
	replaced = []
	#answer = False
	index = 0
	game_string = game_string.split()
	for word in game_string:
		replacement = word_in_blank(word,blanks_in_text)
		if replacement != None:
			user_input = raw_input("Type a " + replacement + " ")
			answer = check_answer(user_input,answers,index)
			'''nada mas incluye las respuestas de los blanks cuando esto es correcto'''
				
			word = word.replace(replacement, user_input)
			replaced.append(word)
	
			index += 1
		else:
			replaced.append(word)

	replaced = " ".join(replaced)
	return replaced

def level_easy():
	easy_answers = ['Ipsum', 'text', '1500s']
	blanks_in_text = ["___1___", "___2___", "___3___", "___4___"]
	easy_para = '''A ___1___ is created with the def keyword. You specify the inputs a ___2___ takes by adding ___3___ separated by commas between the parentheses.'''
	print "The current paragraph is: \n", easy_para
	paragraph = play_game(easy_para,blanks_in_text,easy_answers)

	print paragraph

level = raw_input("Choose a level: easy, medium, or hard.\n")
if level == 'easy':
	print "You chose easy!\n"
	level_easy()
if level == 'medium':
	print 'You chose medium!\n'
if level == 'hard':
	print 'You chose hard!\n'
