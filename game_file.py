print "You walk into a bakery and see many snacks. Do you choose sweet or savory?"

snack = raw_input("> ")

if snack == "sweet":
    print "Baker: 'Ah, a sweet tooth!'\nDo you choose chocolate cake, carrot cake, or red velvet cake?"

    cake = raw_input("> ")

    if cake == "chocolate cake" or cake == "chocolate":
        print "Baker: 'Oh, we're actually sold out of that, sorry. Come back tommorow and try again!' \nYou exit the bakery."
    elif cake == "carrot cake" or cake == "carrot":
        print "Baker: 'Excellent choice.' \nYou take your cake and leave. Bye!"
    elif cake == "red velvet cake" or cake == "red velvet":
        print "The cake was poisoned. You die in agony. Sorry."
    else:
        print "Baker: 'Please choose a cake. We can't keep %s on the shelves!'" % cake
elif snack == "savory":
    print "Baker: 'I see, something with less sugar in it, then. Would you like a meat pie? Quiche? Something...else?'"

    savory = raw_input("> ")

    if savory == "meat pie":
        print "Baker: 'Ham, beef, or long pig?'"

        meat_pie = raw_input("> ")

        if meat_pie == "ham":
            print "You receive a meat pie. Congrat."
        elif meat_pie == "beef":
            print "You receive a meat pie. It's okay."
        elif meat_pie == "long pig":
            print "Baker: 'Are you sure? Well...alright then.'"
            print "You receive your meat pie. It's a little gamey."
        else:
            print "You get nothing. The baker is a busy man, don't waste his time."

    elif savory == "quiche":
        print "Baker: 'Today's quiche is spinach and cheese. Hope you're okay with that.'\nYou receive a slice of quiche."

    #elif savory == "What else?":
    #    print "Oh...uh....nothing."

    elif savory == "something else":
        print "Baker: 'Oh...something else you say? Let me see what we have to offer.'"
        print "Baker: 'We do have some...special items in stock today, but first I gotta ask. You're not the fuzz, are you?'"

        fuzz = raw_input("> ")
        if fuzz == "yes" or fuzz == "yea" or fuzz == "yeah":
            print "Baker: 'Oh, hello officer! Has anybody offered you the police discount?'"
        elif fuzz == "no" or fuzz == "naw" or fuzz == "no way":
            print "Baker: 'Sorry, I had to ask. You understand.'"
            print "You receive a bag of...special herbs."
        else:
            print "Baker: 'Hm. I'm not taking any chances. Come back if you want a pie.'\nYou are escorted out of the bakery."
    else:
        print "Baker: 'If you aren't going to choose something, you should leave.'"

else:
    print "Baker: 'Sorry, we don't have %s today.'\nYou leave the bakery, disappointment evident on your face." % snack
