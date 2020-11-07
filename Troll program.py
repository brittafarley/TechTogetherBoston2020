def main():

    #declare variables
    #initialize variables
    trollSpeak=0
    
    #display welcome message    
    print("Welcome to the Troll Translator!\n")

    #display intro message
    print("Hey you! It's really important that you remember not to feed the [social media] trolls.")
    print("Trolls are misunderstood. Basically, they are people or bots who communicate through misplaced")
    print("anger when they really want to give you a compliment. This handy troll translator will help you")
    print("translate troll-speak to human-speak. Let's go!\n")

    #display instructions
    #display menu
    while True:
        print("Select the troll message that you received.")
        print("The Troll Translator will convert troll-speak.\n")

    
        print("MENU")
        print("1)You are not smart enough!")
        print("2)You are not capable!")
        print("3)You are unattractive!")
        print("4)You will never get it!")
        print("5)Your opinions don't matter!")
        print("6)You don't do enough!")
        print("7)You are too young/old!")
        print("8)Shut up!")
        print("0)Exit translator\n")
        trollSpeak=int(input("Choose a number from the menu:"))
        #error message if user inputs anything else

        #condition statements
        if trollSpeak==1:
            print("Translation:")
            print("You are so intelligent that I feel intimidated by you.")
            print("Putting you down helps me feel better.")
            print("**********************\n")
        elif trollSpeak==2:
            print("Translation:")
            print("I noticed you did something so cool,")
            print("but I'm afraid of giving you a compliment.")
            print("**********************\n")
        elif trollSpeak==3:
            print("Translation:")
            print("You are so unique and bold.")
            print("I feel insecure about my looks and I need someone to feel bad with me.")
            print("**********************\n")
        elif trollSpeak==4:
            print("Translation:")
            print("You are so close to making this breakthrough, so I need to slow you down")
            print("and distract you from working hard.")
            print("**********************\n")
        elif trollSpeak==5:
            print("Translation:")
            print("Your opinions scare me because I know I have to change my narrow views in")
            print("order to be a better person.")
            print("**********************\n")
        elif trollSpeak==6:
            print("Translation:")
            print("You are doing great. You are being efficient at what you do and balancing")
            print("your mental health. I'm incapable of doing that, so I take it out on you instead.")
            print("**********************\n")
        elif trollSpeak==7:
            print("Translation:")
            print("You have unique contributions. Your age does not define your capabilities")
            print("and I applaud that you are breaking down barriers.")
            print("**********************\n")
        elif trollSpeak==8:
            print("Translation:")
            print("I seriously cannot find anything else to say, so I'm being basic. Keep speaking,")
            print("be bold  and never apologize for your authenticity.")
            print("**********************\n")
        elif trollSpeak==0:
            print("Goodbye! Remember don't feed the trolls! They derive happiness from mean-speak.")
            print("You are so much better than that. See you later!")
            break

    



        
