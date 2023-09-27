from PyInquirer import prompt, Separator, style_from_dict
custom_style = style_from_dict({
    "separator": '#6C6C6C',
    "questionmark": '#FF9D00 bold',
    "selected": '#5F819D',
    "pointer": '#FF9D00 bold',
    "instruction": '',  # default
    "answer": '#5F819D bold',
    "question": '',
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
					'message' : '3. What are the common symptoms of COVID-19?',
					'choices' : [
					'Tiredness','A new and continuous cough',
					'Fever',
					'All of the above'
					]
				},
				{
					'type' : 'list',
					'name' : 'HIV',
					'message' : '4. Are people living with HIV always more at risk?',
					'choices' : [
					'No – people who adhere to antiretroviral treatment (ART) and have a high CD4 count aren’t more at risk',
					'Yes – people with HIV have weaker immune systems']
				},
				{
					'type' : 'list',
					'name' : 'peopleInDanger',
					'message' : '5. Which of the following people is COVID-19 more dangerous for?',
					'choices' : [
					'Older people – especially those aged 70 and above',
					'People with certain underlying health conditions',
					'Jordainian people']
				},
				{
					'type' : 'list',
					'name' : 'isCured',
					'message' : '6.Can COVID-19 be cured?',
					'choices' : [
					'No – COVID-19 is a death sentence',
					'Yes – Hot drinks can cure COVID-19',
					'No – but most people get better by themselves']
				},
				{
					'type' : 'list',
					'name' : 'isProtect',
					'message' : '7.Can washing your hands protect you from COVID-19?',
					'choices' : [
					'Yes – but only if you use a strong bleach',
					'No – Washing your hands doesn’t stop COVID-19',
					'Yes – normal soap and water or hand sanitizer is enough']
				},
				{
					'type' : 'list',
					'name' : 'protectHIV',
					'message' : '8.How can people living with HIV protect themselves from COVID-19?',
					'choices' : [
					'Keep taking their antiretroviral treatment',
					'Exercise regularly, eat well and look after their mental health',
					'Wash their hands regularly and follow the physical distancing advice',
					'All of the above']
				},
				{
					'type' : 'list',
					'name' : 'maskWorn',
					'message' : '9.When should fabric face masks be worn?',
					'choices' : [
					'On public transport','In small shops',
					'In confined or crowded spaces',
					'All of the above']
				},
				{
					'type' : 'list',
					'name' : 'distance',
					'message' : '10.Which of the following is an example of physical distancing?',
					'choices' : [
					'You stop going to crowded places and visiting other people’s houses',
					'You stop talking to the people you live with',
					'You stop speaking to your friends on the phone']
				}
			]

answers = prompt.prompt(questions, style=custom_style)


