def e():
    while = True:
        print """

\tGuide Contents:

\t* '%s' - A Standard formatting Syntax to implement varibles into a string easier 
           ("I have %s Cars" % amount)

        """
        raw_input()
        break

    test = True
    while test:
        print "my_name = 'Zed A. Shaw'"
        a = raw_input("> ")
        if a == "my_name = 'Zed A. Shaw'":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "my_age = 35"
        b = raw_input("> ")
        if b == "my_age = 35":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "my_height = 74"
        c = raw_input("> ")
        if c == "my_height = 74":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "my_weight = 180"
        d = raw_input("> ")
        if d == "my_weight = 180":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "my_eyes = 'Blue'"
        e = raw_input("> ")
        if e == "my_eyes = 'Blue'":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "my_teeth = 'White'"
        f = raw_input("> ")
        if f == "my_teeth = 'White'":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "my_hair = 'Brown'"
        g = raw_input("> ")
        if g == "my_hair = 'Brown'":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"Let's talk about %s.\" % my_name"
        h = raw_input("> ")
        if h == "print \"Let's talk about %s.\" % my_name":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"He's %d inches tall.\" % my_height"
        i = raw_input("> ")
        if i == "print \"He's %d inches tall.\" % my_height":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"He's %d pounds heavy.\" % my_weight"
        j = raw_input("> ")
        if j == "print \"He's %d pounds heavy.\" % my_weight":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"Actually that's not too heavy.\""
        k = raw_input("> ")
        if k == "print \"Actually that's not too heavy.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"He's got %s eyes and %s hair.\" % (my_eyes, my_hair)"
        l = raw_input("> ")
        if l == "print \"He's got %s eyes and %s hair.\" % (my_eyes, my_hair)":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"His teeth are usually %s depending on the coffee.\" % my_teeth"
        m = raw_input("> ")
        if m == "print \"His teeth are usually %s depending on the coffee.\" % my_teeth":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"If I add %d, %d, and %d I get %d.\" % (my_age, my_height, my_weight, my_age + my_height + my_weight)"
        n = raw_input("> ")
        if n == "print \"If I add %d, %d, and %d I get %d.\" % (my_age, my_height, my_weight, my_age + my_height + my_weight)":
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
    my_name = 'Zed A. Shaw'
    my_age = 35 #not a lie
    my_height = 74 # inches
    my_weight = 180 # lbs
    my_eyes = 'Blue'
    my_teeth = 'White'
    my_hair = 'Brown'

    print "Let's talk about %s." % my_name
    print "He's %d inches tall." % my_height
    print "He's %d pounds heavy." % my_weight
    print "Actually that's not too heavy."
    print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
    print "His teeth are usually %s depending on the coffee." % my_teeth

    # this line is tricky, try to get it exactly right
    print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
