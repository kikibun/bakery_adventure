nosy_counter = 0
police_officer = False

def pastry():
    global nosy_counter, police_officer
    snack = raw_input("> ")

    if snack == "sweet":
        print "Baker: 'Ah, a sweet tooth!'\nDo you choose chocolate cake, carrot cake, or red velvet cake?"

        cake = raw_input("> ")

        if cake == "chocolate cake" or cake == "chocolate":
            print "Baker: 'Oh, we're actually sold out of that, sorry.'"
            if police_officer == True:
                print "Baker: 'But let me give you this instead to thank you for your service.'\nYou reveive a glazed donut."
                exit(0)
            else:
                print "'Come back tommorow and try again!' \nYou exit the bakery."
                exit(0)
        elif cake == "carrot cake" or cake == "carrot":
            print "Baker: 'Excellent choice.'"
            if police_officer == True:
                print "To your surprise, the baker has drawn your badge in the icing. Nice!"
                exit(0)
            else:
                print "You take your cake and leave. Bye!"
                exit(0)
        elif cake == "red velvet cake" or cake == "red velvet":
            if police_officer == True:
                print "Baker: 'Uh....why don't you take this instead.'\n You received a glazed donut."
                exit(0)
            else:
                print "The cake was poisoned. You die in agony. Sorry."
                exit(0)
        else:
            print "Baker: 'Sorry, we don't have that. Maybe we'll have %s tomorrow!'" % cake
            exit(0)

    elif snack == "savory":
        print "Baker: 'I see, something with less sugar in it, then. Would you like a meat pie? Quiche? Something...else?'"

        savory = raw_input("> ")

        if savory == "meat pie":
            print "Baker: 'Ham, beef, or long pig?'"

            meat_pie = raw_input("> ")

            if meat_pie == "ham":
                if police_officer == True:
                    print "The baker smirks about the irony, but hands you the pie regardless."
                    exit(0)
                else:
                    print "You receive a meat pie. Congrat."
                    exit(0)
            elif meat_pie == "beef":
                if police_officer == True:
                    print "The baker slips a little something in the bag. It's another meat pie! Aw."
                    exit(0)
                else:
                    print "You receive a meat pie. It's okay."
                    exit(0)
            elif meat_pie == "long pig":
                if police_officer == True:
                    print "Baker: 'You know what...why don't you take this instead.'\nYou receive a glazed donut."
                    exit(0)
                else:
                    print "Baker: 'Are you sure? Well...alright then.'"
                    print "You receive your meat pie. It's a little gamey."
                    exit(0)
            else:
                print "You get nothing. The baker is a busy man, don't waste his time."
                exit(0)

        elif savory == "quiche":
            if police_officer == True:
                print "Baker: 'We've got an armed forces special in the back, let me go grab it.'\nYou receive a slice of tomato bacon quiche."
                exit(0)
            else:
                print "Baker: 'Today's quiche is spinach and cheese. Hope you're okay with that.'\nYou receive a slice of quiche."
                exit(0)

        elif savory in ["What else?", "what else", "what else?"]:
            print "Baker: 'Oh...uh....nothing. Did you still want something sweet or savory?'"
            nosy_counter += 1
            if nosy_counter == 2:
                print "Baker: 'You ask too many questions. Come back when you know what you want.'\nThe baker glares at you until you leave."
                exit(0)
            pastry()

        elif savory == "something else":
            if police_officer == True and nosy_counter < 1:
                nosy_counter += 1
                print "Baker: 'Sorry officer, we don't have any specials today. Could I offer you something sweet, or something savory?'\nThe baker sweats nervously."
                pastry()
            elif police_officer == True and nosy_counter == 1:
                print "Baker: 'You know, I really should get to my other customers. Come back any time.'\nYou take the hint, and leave."
                exit(0)
            elif police_officer == False:
                print "Baker: 'Oh...something else you say? Let me see what we have to offer.'"
                print "Baker: 'We do have some...special items in stock today, but first I gotta ask. You're not the fuzz, are you?'"

            fuzz = raw_input("> ")
            if fuzz in ["yea", "yes", "yeah"]:
                police_officer = True
                print "Baker: 'Oh, hello officer! Has anybody offered you the police discount? Something sweet or savory today?'"
                pastry()
            elif fuzz in ["no", "naw", "no way"]:
                print "Baker: 'Sorry, I had to ask. You understand.'"
                print "You receive a bag of...special herbs."
                exit(0)
            else:
                print "Baker: 'Hm. I'm not taking any chances. Come back if you want a pie.'\nYou are escorted out of the bakery."
                exit(0)
        else:
            print "Baker: 'If you aren't going to choose something, you should leave.'"
            exit(0)

    else:
        print "Baker: 'Sorry, we don't have %s today.'\nYou leave the bakery, disappointment evident on your face." % snack
        exit(0)

print "You walk into a bakery and see many snacks. Do you choose sweet or savory?"
pastry()
