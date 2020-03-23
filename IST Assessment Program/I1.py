def a():
    while = True:
        print """

\tGuide Contents:

\t* raw_input() = Gives the user the option to input data to the user, 
                  anything inbetween the '()' will be displayed before 
                  the users input.

        """
        raw_input()
        break

    test = True
    while test:
        print "print \"How old are you?\","
        a = raw_input("> ")
        if a == "print \"How old are you?\",":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "age = raw_input()"
        b = raw_input("> ")
        if b == "age = raw_input()":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"How tall are you?\","
        c = raw_input("> ")
        if c == "print \"How tall are you?\",":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "height = raw_input()"
        d = raw_input("> ")
        if d == "height = raw_input()":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"How much do you weigh?\","
        e = raw_input("> ")
        if e == "print \"How much do you weigh?\",":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "weight = raw_input()"
        f = raw_input("> ")
        if f == "weight = raw_input()":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"So, you're %r old, %r tall and %r heavy.\" % (age, height, weight)"
        g = raw_input("> ")
        if g == "print \"So, you're %r old, %r tall and %r heavy.\" % (age, height, weight)":
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
    Exit = raw_input()

    print "This is what would happen if you ran it."
    print "How old are you?",
    age = raw_input()
    print "How tall are you?",
    height = raw_input()
    print "How much do you weigh?",
    weight = raw_input()

    print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

