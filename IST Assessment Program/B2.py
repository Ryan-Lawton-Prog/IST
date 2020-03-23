def b():
    while = True:
        print """

\tGuide Contents:

\t* # stuff - What ever is placed after the '#' will be not classified as code.
              You can use this to help people who are reading over your code to know what it does.

        """
        raw_input()
        break
    test = True
    while test:
        print "# A comment, this is so you can read your program later."
        a = raw_input("> ")
        if a == "# A comment, this is so you can read your program later.":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "# Anything after the # is ignored by Python"
        b = raw_input("> ")
        if b == "# Anything after the # is ignored by Python":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"I could have code like this.\" # and the comment after is ignored"
        c = raw_input("> ")
        if c == "print \"I could have code like this.\" # and the comment after is ignored":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "# You can also use a comment to \"disable\" or comment out a piece of code:"
        d = raw_input("> ")
        if d == "# You can also use a comment to \"disable\" or comment out a piece of code:":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "# print \"This won't run.\""
        e = raw_input("> ")
        if e == "# print \"This won't run.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"This will run.\""
        f = raw_input("> ")
        if f == "print \"This will run.\"":
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
    Exit = raw_input()

    print "This is what would happen if you ran it."
    print ""
    # A comment,this is so you can read your program later.
    # Anything after the # is ignored by Python
    print "I could have code like this." # and the comment after is ignored
    # You can also use a comment to "disable" or comment out a piece of code:
    # print "This won't run."
    print "This will run."
    Exit = raw_input()
