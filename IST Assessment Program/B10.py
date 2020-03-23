def j():

    test = True
    while test:
        print "tabby_cat = \"\\tI'm tabbed in.\""
        a = raw_input("> ")
        if a == "tabby_cat = \"\\tI'm tabbed in.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "persian_cat = \"I'm split\\non a line.\""
        b = raw_input("> ")
        if b == "persian_cat = \"I'm split\\non a line.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "backslash_cat = \"I'm \\\\ a \\\\ cat.\""
        c = raw_input("> ")
        if c == "backslash_cat = \"I'm \\\\ a \\\\ cat.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "fat_cat = \"\"\""
        d = raw_input("> ")
        if d == "fat_cat = \"\"\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "I'll do a list:"
        e = raw_input("> ")
        if e == "I'll do a list:":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "\\t* Cat food"
        f = raw_input("> ")
        if f == "\\t* Cat food":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "\\t* Fishies"
        g = raw_input("> ")
        if g == "\\t* Fishies":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "\\t* Catnip\\n\\t* Grass"
        h = raw_input("> ")
        if h == "\\t* Catnip\\n\\t* Grass":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "\"\"\""
        i = raw_input("> ")
        if i == "\"\"\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print tabby_cat"
        j = raw_input("> ")
        if j == "print tabby_cat":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print persian_cat"
        k = raw_input("> ")
        if k == "print persian_cat":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print backslash_cat"
        l = raw_input("> ")
        if l == "print backslash_cat":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print fat_cat"
        m = raw_input("> ")
        if m == "print fat_cat":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    print "You have wrote"
    print ""
    print a
    print b
    print c
    print d
    print e
    print f
    print g
    print h
    print i
    print j
    print k
    print l
    print m
    Exit = raw_input()

    print "This is what would happen if you ran it."
    tabby_cat = "\tI'm tabbed in."
    persian_cat = "I'm split\non a line."
    backslash_cat = "I'm \\ a \\ cat."

    fat_cat = """
    I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
    """

    print tabby_cat
    print persian_cat
    print backslash_cat
    print fat_cat
