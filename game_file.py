print "You walk into a bakery and see many snacks. Do you choose sweet or savory?"

snack = raw_input("> ")

if snack == "sweet":
    print "Ah, a sweet tooth! Do you choose chocolate cake, carrot cake, or red velvet cake?"

    cake = raw_input("> ")

    if cake == "chocolate cake":
        print "Oh, we're actually sold out of that, sorry. Come back tommorow and try again!"
    elif cake == "carrot cake":
        print "Great choice. You take your cake and leave. Bye!"
    elif cake == "red velvet cake":
        print "The cake was poisoned. You die in agony. Sorry."
    else:
        print "Please choose a cake."
elif snack == "savory":
    print "I see, something with less sugar in it, then. Would you like a meat pie? Quiche? Something...else?"

    savory = raw_input("> ")

    if savory == "meat pie":
        print "Ham, beef, or long pig?"

        meat_pie = raw_input("> ")

        if meat_pie == "ham":
            print "You receive a meat pie. Congrat."
        elif meat_pie == "beef":
            print "You receive a meat pie. It's okay."
        elif meat_pie == "long pig":
            print "Are you sure? Well...alright then."
            print "You receive your meat pie. It's a little gamey."
        else:
            print "You get nothing."

    elif savory == "quiche":
        print "Today's quiche is spinach and cheese. Hope you're okay with that."
        print "You receive a slice of quiche."

    #elif savory == "What else?":
    #    print "Oh...uh....nothing."

    elif savory == "something else":
        print "Oh...something else you say? Let me see what we have to offer."

    else:
        print "If you aren't going to choose something, you should leave."

else:
    print "Sorry, we don't have %s today." % snack
