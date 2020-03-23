def f():
    while = True:
        print """

\tGuide Contents:

\t* '%d' - A format that is used for debugging.
\t* '%r' - A format that is used for not convverting code to string like '%s' does but gives it raw.

        """
        raw_input()
        break

    test = True
    while test:
        print "x = \"There are %d types of people.\" % 10"
        a = raw_input("> ")
        if a == "x = \"There are %d types of people.\" % 10":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "binary = \"binary\""
        b = raw_input("> ")
        if b == "binary = \"binary\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "do_not = \"don't\""
        c = raw_input("> ")
        if c == "do_not = \"don't\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "y = \"Those who know %s and those who %s.\" % (binary, do_not)"
        d = raw_input("> ")
        if d == "y = \"Those who know %s and those who %s.\" % (binary, do_not)":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print x"
        e = raw_input("> ")
        if e == "print x":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print y"
        f = raw_input("> ")
        if f == "print y":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"I said: %r.\" % x"
        g = raw_input("> ")
        if g == "print \"I said: %r.\" % x":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"I also said: '%s'.\" % y"
        h = raw_input("> ")
        if h == "print \"I also said: '%s'.\" % y":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "hilarious = False"
        i = raw_input("> ")
        if i == "hilarious = False":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "joke_evaluation = \"Isn't that joke so funny?! %r\""
        j = raw_input("> ")
        if j == "joke_evaluation = \"Isn't that joke so funny?! %r\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print joke_evaluation % hilarious"
        k = raw_input("> ")
        if k == "print joke_evaluation % hilarious":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "w = \"This is the left side of...\""
        l = raw_input("> ")
        if l == "w = \"This is the left side of...\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "e = \"a string with a right side.\""
        m = raw_input("> ")
        if m == "e = \"a string with a right side.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print w + e"
        n = raw_input("> ")
        if n == "print w + e":
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
    print n
    Exit = raw_input()

    print "This is what would happen if you ran it."
    print ""
    x = "There are %d types of people." % 10
    binary = "binary"
    do_not = "don't"
    y = "Those who know %s and those who %s." % (binary, do_not)

    print x
    print y

    print "I said: %r." % x
    print "I also said: '%s'." % y

    hilarious = False
    joke_evaluation = "Isn't that joke so funny?! %r"

    print joke_evaluation % hilarious

    w = "This is the left side of..."
    e = "a string with a right side."

    print w + e
