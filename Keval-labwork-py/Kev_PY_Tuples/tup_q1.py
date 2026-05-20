people= [('Kavy','Jineet'),('Kelin','Keval'),('Aryan'), 'Alexa','Siri','Gemini']
boys_count= sum(len(person) for person in people if isinstance(person,tuple))
girls_count= sum(1 for person in people if isinstance(person,str))
print("No. of boys are ", boys_count)
print("No. of girls are ", girls_count)
