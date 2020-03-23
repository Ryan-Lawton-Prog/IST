def a():
    while = True:
        print """

\tGuide Contents:

\t* Print "stuff" - Shows what ever is inbetween the quotation marks in command prompt.
\t* Print 'stuff' - Shows what ever is inbetween the quotation marks in command prompt.

        """
        raw_input()
        break
    test = True
    while test:
        print "print \"Hello World!\""
        a = raw_input("> ")
        if a == "print \"Hello World!\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"Hello Again\""
        b = raw_input("> ")
        if b == "print \"Hello Again\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"I like typing this.\""
        c = raw_input("> ")
        if c == "print \"I like typing this.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"This is fun.\""
        d = raw_input("> ")
        if d == "print \"This is fun.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:            
        print 'print \'Yay! Printing.\''
        e = raw_input("> ")
        if e == 'print \'Yay! Printing.\'':
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"I'd much rather you 'not'.\""
        f = raw_input("> ")
        if f == "print \"I'd much rather you 'not'.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print 'print \'I "said" do not touch this.\''
        g = raw_input("> ")
        if g == 'print \'I "said" do not touch this.\'':
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
    print ""
    print "Hello World!"
    print "Hello Again"
    print "I like typing this."
    print "This is fun."
    print 'Yay! Printing.'
    print "I'd much rather you 'not'."
    print 'I "said" do not touch this.'
    Exit = raw_input()
