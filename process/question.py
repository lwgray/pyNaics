def question(sector):
    for index, i in enumerate(words[sector].keys()):
        print index, i
        addit = raw_input("Add {0}".format(i))
        addit = addit.lower()
        if addit == 'y' or  addit == 'yes':
            print i
        subtractit = raw_input("Subtract {0}".format(i))
        subtractit.lower()
        if subtractit == 'y' or subtractit == 'yes':
            print i
    return

