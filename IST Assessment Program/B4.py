def d():
    while = True:
        print """

\tGuide Contents:

\t* Variables - Assigning a value (string, float, number etc.) to a word or phrase
                (Truck = "Red", Cats = 5, Pi = 3.14159265) 

        """
        raw_input()
        break
    test = True
    while test:
        print "print \"This is what would happen if you ran it.\""
        a = raw_input("> ")
        if a == "print \"This is what would happen if you ran it.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "cars = 100"
        b = raw_input("> ")
        if b == "cars = 100":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "space_in_a_car = 4.0"
        c = raw_input("> ")
        if c == "space_in_a_car = 4.0":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "drivers = 30"
        d = raw_input("> ")
        if d == "drivers = 30":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "passengers = 90"
        e = raw_input("> ")
        if e == "passengers = 90":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "cars_not_driven = cars - drivers"
        f = raw_input("> ")
        if f == "cars_not_driven = cars - drivers":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "cars_driven = drivers"
        g = raw_input("> ")
        if g == "cars_driven = drivers":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "carpool_capacity = cars_driven * space_in_a_car"
        h = raw_input("> ")
        if h == "carpool_capacity = cars_driven * space_in_a_car":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "average_passengers_per_car = passengers / cars_driven"
        i = raw_input("> ")
        if i == "average_passengers_per_car = passengers / cars_driven":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"There are\", cars, \"cars available.\""
        j = raw_input("> ")
        if j == "print \"There are\", cars, \"cars available.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"There are only\", drivers, \"drivers available.\""
        k = raw_input("> ")
        if k == "print \"There are only\", drivers, \"drivers available.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"There will be\", cars_not_driven, \"empty cars today.\""
        l = raw_input("> ")
        if l == "print \"There will be\", cars_not_driven, \"empty cars today.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"We can transport\", carpool_capacity, \"people today.\""
        m = raw_input("> ")
        if m == "print \"We can transport\", carpool_capacity, \"people today.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"We have\", passengers, \"to carpool today.\""
        n = raw_input("> ")
        if n == "print \"We have\", passengers, \"to carpool today.\"":
            test = False
            print ""
        else:
            print "Please Check Over Your Code"
            print ""

    test = True
    while test:
        print "print \"We need to put about\", average_passengers_per_car, \"in each car.\""
        o = raw_input("> ")
        if o == "print \"We need to put about\", average_passengers_per_car, \"in each car.\"":
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
    print o
    Exit = raw_input()

    print "This is what would happen if you ran it."
    cars = 100
    space_in_a_car = 4.0
    drivers = 30
    passengers = 90
    cars_not_driven = cars - drivers
    cars_driven = drivers
    carpool_capacity = cars_driven * space_in_a_car
    average_passengers_per_car = passengers / cars_driven

    print "There are", cars, "cars available."
    print "There are only", drivers, "drivers available."
    print "There will be", cars_not_driven, "empty cars today."
    print "We can transport", carpool_capacity, "people today."
    print "We have", passengers, "to carpool today."
    print "We need to put about", average_passengers_per_car, "in each car."
