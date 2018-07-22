import sys

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    answers = range(1,9)
    print (answers)
    if (question == ""):
        sys.exit()
	elif (answers == answers[0]):
        print ( "It is certain")
    
    elif (answers == answers[1]):
        print ( "Outlook good")
    
    elif (answers == answers[2]):
        print ( "You may rely on it")
    
    elif (answers == answers[3]):
        print ( "Ask again later")
    
    elif (answers == answers[4]):
        print ( "Concentrate and ask again")
    
    elif (answers == answers[5]):
        print ( "Reply hazy, try again")
    
    elif (answers == answers[6]):
        print ( "My reply is no")
    
    elif (answers == answers[7]):
        print ( "My sources say no")