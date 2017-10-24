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

# def guesses(guess):
# 	number = 5
# 	while number > 0:
# 		if guess == False:
# 			number -= 1
# 			return number 
# 		else:
# 			return number
	# if guess == False:
	# 	number -= 1
	# 	return number 

def play_game(game_string, blanks_in_text, answers, max_guesses):
	replaced = []
	answer = False
	index = 0
	game_string = game_string.split()
	for word in game_string:
		replacement = word_in_blank(word,blanks_in_text)
		if replacement != None:
			while not answer and max_guesses != 0:
				user_input = raw_input("Type a " + replacement + " ")
				answer = check_answer(user_input,answers,index, max_guesses)
				if not answer:
					max_guesses -= 1
				if max_guesses == 0:
					sys.exit("Game over")
			word = word.replace(replacement, user_input)
			replaced.append(word)
			index += 1
			answer = False
		else:
			replaced.append(word)

	replaced = " ".join(replaced)
	return replaced

def level_easy():
	easy_answers = ['Ipsum', 'text', '1500s']
	blanks_in_text = ["___1___", "___2___", "___3___", "___4___"]
	easy_para = '''A ___1___ is created with the def keyword. You specify the inputs a ___2___ takes by adding ___3___ separated by commas between the parentheses.'''
	numb_of_wrong_guesses = 5
	print "The current paragraph is: \n", easy_para
	paragraph = play_game(easy_para,blanks_in_text,easy_answers, numb_of_wrong_guesses)

	print paragraph

level = raw_input("Choose a level: easy, medium, or hard.\n")
if level == 'easy':
	print "You chose easy!\n"
	print "You have a total of 5 guesses"
	level_easy()
if level == 'medium':
	print 'You chose medium!\n'
if level == 'hard':
	print 'You chose hard!\n'