def h():

    test = True
    while test:
        print "formatter = \"%r %r %r %r\""
        a = raw_input("> ")
        if a == "formatter = \"%r %r %r %r\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print formatter % (1, 2, 3, 4)"
        b = raw_input("> ")
        if b == "print formatter % (1, 2, 3, 4)":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print formatter % (\"one\", \"two\", \"three\", \"four\")"
        c = raw_input("> ")
        if c == "print formatter % (\"one\", \"two\", \"three\", \"four\")":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print formatter % (True, False, False, True)"
        d = raw_input("> ")
        if d == "print formatter % (True, False, False, True)":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print formatter % (formatter, formatter, formatter, formatter)"
        e = raw_input("> ")
        if e == "print formatter % (formatter, formatter, formatter, formatter)":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print formatter % ("
        f = raw_input("> ")
        if f == "print formatter % (":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "\"I had this thing.\","
        g = raw_input("> ")
        if g == "\"I had this thing.\",":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "\"That you could type up right.\","
        h = raw_input("> ")
        if h == "\"That you could type up right.\",":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "\"But it didn't sing.\","
        i = raw_input("> ")
        if i == "\"But it didn't sing.\",":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "\"So I said goodnight.\""
        j = raw_input("> ")
        if j == "\"So I said goodnight.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print ")"
        k = raw_input("> ")
        if k == ")":
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
    Exit = raw_input()

    print "This is what would happen if you ran it."
    formatter = "%r %r %r %r"

    print formatter % (1, 2, 3, 4)
    print formatter % ("one", "two", "three", "four")
    print formatter % (True, False, False, True)
    print formatter % (formatter, formatter, formatter, formatter)
    print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
    )
