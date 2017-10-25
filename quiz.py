import sys


def word_in_blank(word, blanks_in_text):
	"""looks for presence of specific blanks within the given paragraphs"""
	for n in blanks_in_text:
		if n in word:
			return n
	return None

def check_answer(user_guess,answer_list,word_position, max_guesses):
	if user_guess == answer_list[word_position]:
		print "Correct!\n"
		return True
	else:
		print "Incorrecto!", "You have a total of "+ str(max_guesses - 1) + " guesses"

def ask_questions(para,word_to_replace,list_answer,numb_of_guesses,index):
	answer = False
	while not answer and numb_of_guesses != 0:
		user_input = raw_input("Type a " + word_to_replace + " ")
		answer = check_answer(user_input,list_answer,index,numb_of_guesses)
		if not answer:
			numb_of_guesses -= 1
			print para
		if numb_of_guesses == 0:
			sys.exit("You ran out of guesses! Sorry, game over")
	return user_input

def change_multiple_blanks(blank, list_level_para):
	offset = 0
	indices = list()
	for i in range(list_level_para.count(blank)):
		indices.append(list_level_para.index(blank,offset))
		offset = indices[-1] + 1
	return indices 


def play_game(game_string, blanks_in_text, answers, max_guesses):
	index = 0
	game_string = game_string.split()
	for word in game_string:
		replacement = word_in_blank(word,blanks_in_text)
		if replacement != None:
			'''assings a number to index_to_change, depending on what index number replacement is''' 
			blanks_in_para = change_multiple_blanks(replacement,game_string)
			user_input = ask_questions(replacement,answers,max_guesses,index)
			word = word.replace(replacement, user_input)
			'''changes element in list game_string to the value of variable word, above'''
			for i in blanks_in_para:
				game_string[i] = word
			'''converts list game_string into a string'''
			game_string = " ".join(game_string)
			print game_string
			'''splits game_string again to find the next number in the list'''
			game_string = game_string.split()
			index += 1

def level_easy():
	numb_of_wrong_guesses = int(raw_input("how many guesses for this question? "))

	easy_para = '''A ___1___ is created with the ___1___ keyword. You specify the inputs a ___2___ takes by adding ___3___ separated by commas between the parentheses.'''
	print "The current paragraph is: \n", easy_para
	blanks_in_text = ["___1___", "___2___", "___3___", "___4___"]
	easy_answers = ['Ipsum','text', '1500s']

	paragraph = play_game(easy_para,blanks_in_text,easy_answers, numb_of_wrong_guesses)

def level_medium():
	medium_answers = ['Bolivar', 'Venezuela']
	blanks_in_text = ["___1___", "___2___"]
	medium_para = '''Simon ___1___ Caracas, ___2___ '''
	'''asks the user the number of guesses per question. Assings raw_input to variable numb_of_wrong_guesses than then it's passed to play_game as an arguemtn)'''
	numb_of_wrong_guesses = int(raw_input("how many guesses for this questions? "))

	print "The current paragraph is: \n", medium_para
	paragraph = play_game(medium_para,blanks_in_text,medium_answers, numb_of_wrong_guesses)
	#print paragraph


level = raw_input("Choose a level: easy, medium, or hard.\n")
if level == 'easy':
	print "You chose easy!\n"
	level_easy()
if level == 'medium':
	print 'You chose medium!\n'
	level_medium()
if level == 'hard':
	print 'You chose hard!\n'






