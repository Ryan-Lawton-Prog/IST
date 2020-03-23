def b():
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
        print "age = raw_input(\"How old are you? \")"
        a = raw_input("> ")
        if a == "age = raw_input(\"How old are you? \")":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "height = raw_input(\"How tall are you? \")"
        b = raw_input("> ")
        if b == "height = raw_input(\"How tall are you? \")":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "weight = raw_input(\"How much do you weigh? \")"
        c = raw_input("> ")
        if c == "weight = raw_input(\"How much do you weigh? \")":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"So, you're %r old, %r tall and %r heavy.\" % (age, height, weight)"
        d = raw_input("> ")
        if d == "print \"So, you're %r old, %r tall and %r heavy.\" % (age, height, weight)":
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
    Exit = raw_input()

    print "This is what would happen if you ran it."
    age = raw_input("How old are you? ")
    height = raw_input("How tall are you? ")
    weight = raw_input("How much do you weigh? ")

    print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


