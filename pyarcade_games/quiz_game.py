from PyInquirer import style_from_dict, Token
from PyInquirer.prompt import prompt
from pyfiglet import Figlet
import readchar
import time
import sys
import os
import readchar
from pyarcade_games.save_data import save_data, retrive_value
style = style_from_dict({
	Token.Separator : '#fff',      #white
	Token.QuestionMark : '#000',   #black
	Token.Selected : '#00BFFF',    #sky blue
	Token.Pointer : '#fff',        #white
	Token.Instruction : '#fff',    #white
	Token.Answer : '#008000 bold', #green
	Token.Question : '#FF7F50',    #shade of orange
})

questions = [
				{
					'type' : 'list',
					'name' : 'howPass',
					'message' : '1. How is COVID-19 passed on?',
					'choices' : [
					'In sexual fluids, including semen, vaginal fluids or anal mucous',
					'By drinking unclean water',
					'Through droplets that come from your mouth and nose when you cough or breathe out',
					'All of the above'
					]
				},
				{
					'type' : 'list',
					'name' : 'isPositve',
					'message' : '2. Can you always tell if someone has COVID-19?',
					'choices' : [
					'Yes – it will be obvious, a person with COVID-19 coughs a lot',
					'Yes – you can tell just by where a person comes from, their race and ethnicity',
					'No – not everyone with COVID-19 has symptoms'
					]
				},
				{
					'type' : 'list',
					'name' : 'symptoms',
					'message' : '3. What are the common symptoms of COVID-19? ',
					'choices' : [
					'Tiredness','A new and continuous cough',
					'Fever',
					'All of the above'
					]
				},
				{
					'type' : 'list',
					'name' : 'HIV',
					'message' : '4. Are people living with HIV always more at risk? ',
					'choices' : ['No – people who adhere to antiretroviral treatment (ART) and have a high CD4 count aren’t more at risk','Yes – people with HIV have weaker immune systems']
				},
				{
					'type' : 'list',
					'name' : 'peopleInDanger',
					'message' : '5. Which of the following people is COVID-19 more dangerous for?',
					'choices' : ['Older people – especially those aged 70 and above','People with certain underlying health conditions','Jordainian people']
				},
				{
					'type' : 'list',
					'name' : 'isCured',
					'message' : '6.Can COVID-19 be cured?',
					'choices' : ['No – COVID-19 is a death sentence','Yes – Hot drinks can cure COVID-19','No – but most people get better by themselves']
				},
				{
					'type' : 'list',
					'name' : 'isProtect',
					'message' : '7.Can washing your hands protect you from COVID-19?',
					'choices' : ['Yes – but only if you use a strong bleach','No – Washing your hands doesn’t stop COVID-19','Yes – normal soap and water or hand sanitizer is enough']
				},
				{
					'type' : 'list',
					'name' : 'protectHIV',
					'message' : '8.How can people living with HIV protect themselves from COVID-19?',
					'choices' : ['Keep taking their antiretroviral treatment','Exercise regularly, eat well and look after their mental health','Wash their hands regularly and follow the physical distancing advice','All of the above']
				},
				{
					'type' : 'list',
					'name' : 'maskWorn',
					'message' : '9.When should fabric face masks be worn?',
					'choices' : ['On public transport','In small shops','In confined or crowded spaces','All of the above']
				},
				{
					'type' : 'list',
					'name' : 'distance',
					'message' : '10.Which of the following is an example of physical distancing?',
					'choices' : ['You stop going to crowded places and visiting other people’s houses','You stop talking to the people you live with','You stop speaking to your friends on the phone']
				}
			]
correct_answers = [
	'Through droplets that come from your mouth and nose when you cough or breathe out',
	'No – not everyone with COVID-19 has symptoms',
	'All of the above',
	'No – people who adhere to antiretroviral treatment (ART) and have a high CD4 count aren’t more at risk',
	'Older people – especially those aged 70 and above',
	'No – but most people get better by themselves',
	'Yes – normal soap and water or hand sanitizer is enough',
	'All of the above',
	'All of the above',
	'You stop going to crowded places and visiting other people’s houses',
]
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
def get_answers():
    """
    Get Answers method for prompt user answers by showing questions in sequeance
    * Arg: Takes no arguments
    
    * Sub-Methods: 
        prompt(): method from PyInquirer takes tow arguments for prompt process
            Arg: 
                questions: questions as Array of objects consist of type, name, message and choices
                style: style_from_dict method invokation passing object of Token instances configuration
    * Return:
        answers: object of keys and values for the name of quistion and the choice of user 
                  
    """
    answers = prompt(questions,style = style)
    return answers
def get_score(solutions,user_solution):
    """
    Get score method for calculation of the mark of quiz

    Arg:
        solutions : array of strings for the correct answers 
        user_solution : dictionary of objects that contain key value pairs 
        of the question name and user answer
    Return : 
        score : Integer number from 0-9 for the score of game
    """
    score = 0
    for s,u in zip(solutions,user_solution):
        if s == u:
            score += 1
    return score
def display(msg,style):
    """
    Display function for ASCII art text generation 

    Arg: 
        msg: string argument for the messege to be printed
        style: special argument to select the style of messge to be printed
    Return:
        result : a messege in ASCII art style
    """
    f = Figlet(font=style)
    result=f.renderText(msg)
    print(result)
    return result
def main():
	"""
    Main function for Runinng the game
    Arg: 
    No Argument
    Return:
    No return Value
    """
	display("     Covid-19 Quiz Game","small")	
	print('Enter s to start the game, q to exit : ')
	char=readchar.readchar()
	if char=='s':
		# ------------------------- Play ------------------------------
		display("     Quiz Game","small")
		print("Welcome to the quiz game, we have 10 questions to answer and you will get your score at the end, Good Luck!")
		clear_console()
		userAnswers = get_answers()
		time.sleep(1)
		# -------------------------- Game End ------------------------------
		user_answers = [j for j in userAnswers.values()]
		score = get_score(correct_answers,user_answers)
		existing_score = retrive_value("quizgame_score")
		if existing_score and existing_score > score:
			pass
		else:
			save_data("quizgame_score",score)
		clear_console()
		display(f"Your Score : {score} of 10","small")
		time.sleep(3)
		print("Do you want to back main menu (b) or exit (e)")
		char2=readchar.readchar()
		if char2=='b': 
			print("Back to main menu..")
			time.sleep(2)
			command = 'python -m main'
			os.system(command)
		elif char2=='e':
			print("Quit from game..")
			time.sleep(1)
			os.system('exit')
	elif char=='q':
		os.system('exit')
