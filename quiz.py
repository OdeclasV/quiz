import sys 


def word_in_blank(word, blanks_in_text):
	'''looks for presence of specific blanks within the given paragraphs'''
	for n in blanks_in_text:
		if n in word:
			return n
	return None

def check_answer(user_guess,answer_list,word_position, max_guesses):
	'''checks user's answers to specific blanks, using a list of answers and the indexes in that list, to check if they are correct or incorrect. Prints confirmation to the user and returns True'''
	if user_guess == answer_list[word_position]:
		print "Correct! Good job!\n"
		return True
	else:
		print "Incorrect! please try again.", "You have a total of "+ str(max_guesses - 1) + " guesses"

def ask_questions(word_to_replace,list_answer,numb_of_guesses,index):
	'''asks for user input to the user to replace the blanks in the specific paragraph. This function takes the return from check_answer (above) that changes variable 'answer' to True. If answers is incorrect, subtracts one from numb_of_guesses and asks the question again. If answer is correct, returns it to be used in play_game(), below.'''
	answer = False
	while not answer and numb_of_guesses != 0: #while answer is False and numb_of_guesses is not 0
		user_input = raw_input("What should go on " + word_to_replace + "? ")
		answer = check_answer(user_input,list_answer,index,numb_of_guesses)
		if not answer:
			numb_of_guesses -= 1
		if numb_of_guesses == 0:
			sys.exit("You've ran out of guesses! Sorry, game over") #this is used to stop the game when numb_of_guesses is equal to 0
	return user_input

def change_multiple_blanks(blank, list_level_para):
	'''takes the index of multiple similar blanks in a specific paragraph. This is done in case there are more that one similar blanks/words that need to be changed at the same time. Function retursn, in a list, the indices of elements found'''
	offset = 0
	indices = list()
	for i in range(list_level_para.count(blank)):
		indices.append(list_level_para.index(blank,offset))
		offset = indices[-1] + 1
	return indices 


def play_game(game_string, blanks_in_text, answers, max_guesses):
	'''changes and adds answers to each blank into the specific paragraph for each level. As inputs, takes inforamtion from a level in the game, depending on which one the user chooses.'''
	index = 0
	game_string = game_string.split()
	for word in game_string:
		replacement = word_in_blank(word,blanks_in_text) #string of specific element in paragraph found from list blank_in_text
		if replacement != None:
			blanks_in_para = change_multiple_blanks(replacement,game_string) #list of indeces of multiple blanks to change
			user_input = ask_questions(replacement,answers,max_guesses,index) #string of correct answer to specific blank
			word = word.replace(replacement, user_input) #assings variable word to user_input above
			for i in blanks_in_para: #changes element in list game_string to the value of variable word, above
				game_string[i] = word
			game_string = " ".join(game_string) #converts list game_string into a string
			print game_string
			game_string = game_string.split() #splits game_string again to find the next number in the list
			index += 1

def level_easy():
	'''information for level easy paragraph and answers. Takes no inputs as I want it to exectue as every time the user chooses it without passing any specific information as inputs'''
	numb_of_wrong_guesses = int(raw_input("how many tries would you like to have for this level? ")) #asks the user the number of guesses per question. Assings raw_input to variable numb_of_wrong_guesses than then it's passed to play_game as an arguemtn)
	easy_para = '''___1___ is a short, pudgy, Italian plumber who wears a red hat and blue overalls and resides in the Mushroom Kingdom. The ___1___ franchise is the best-selling video game franchise of all time, created by the ___2___ company. His adventures generally center upon rescuing Pricess ___3___ from his archenemy ___4___ sometimes with help from ___5___ his brother.'''
	print "The current paragraph is: \n", easy_para #print current paragraph to the suse at the start of the game
	blanks_in_text = ["___1___", "___2___", "___3___", "___4___", "___5___"]
	easy_answers = ['Mario','Nintendo', 'Peach', 'Bowser', 'Luigi']

	paragraph = play_game(easy_para,blanks_in_text,easy_answers, numb_of_wrong_guesses) #calls play_game with these values as inputs

def level_medium():
	'''same as level_easy() function above'''
	numb_of_wrong_guesses = int(raw_input("how many tries would you like to have for this level? "))
	medium_para = '''The legend of ___1___ centers of Link, the chief protagonist, tasked with rescuing Princess ___1___ and the kingdom of Hyrule. The original game was released in ___2___ and is now one of Nintendo's most prominent and successful franchises. Ocarina of ___3___ remains one of the most critically acclaimed video games for Nintendo, with several other games in the series also earning high marks. In 2006, Nintendo developers hand to make Link ___4___ -handed to make use of new functionalities in the Nintendo Wii.   '''
	print "The current paragraph is: \n", medium_para
	blanks_in_text = ["___1___", "___2___", "___3___", "___4___"]
	medium_answers = ['Zelda', '1986', 'time','right' ]
	
	paragraph = play_game(medium_para,blanks_in_text,medium_answers, numb_of_wrong_guesses)

def level_hard():
	'''same as level_easy() function above'''
	numb_of_wrong_guesses = int(raw_input("how many tries would you like to have for this level? "))
	hard_para = '''___1___ Aran is the protagonist of the ___2___ action-adventure game series by Nintendo. She is well-know as of the earliest female protagonists in video game history, and inspiration for the game came from Ridley Scott's film ___3___ which was very popular at that time. She was introduced in the ___4___ video game Metroid. '''
	print "The current paragraph is: \n", hard_para
	blanks_in_text = ["___1___", "___2___", "___3___", "___4___"]
	hard_answers = ['Samus', 'Metroid', 'Alien','1986']
	
	paragraph = play_game(hard_para,blanks_in_text,hard_answers, numb_of_wrong_guesses)


'''starts game by asking the user the specific level they'd like to play. Given user's answer, a level related to each function it's called '''
level = raw_input("Choose a level: easy, medium, or hard.\n")
if level == 'easy':
	print "You chose easy!\n"
	level_easy()
if level == 'medium':
	print 'You chose medium!\n'
	level_medium()
if level == 'hard':
	print 'You chose hard!\n'
	level_hard()






