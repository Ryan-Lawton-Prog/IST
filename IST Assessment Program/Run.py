import Beginner

# Program Varriable is now True
Program = True

# 'while' Program is true run and loop this
while Program:

    # select your difficulty text
    print "Please select your Stream"
    print "Beginner:"
    print "Intermediate:"
    print "Advanced:"
    
    # difficulty input
    Difficulty = raw_input("> ")
    
    # 'if' difficulty is 'Beginner':
    if Difficulty == "Beginner":
        print "Please select your exercise"
        print """
\t* Intro:
\t* 1: A Good First Program
\t* 2: Comments And Pound Characters
\t* 3: Numbers And Math
\t* 4: Variables And Names
\t* 5: More Variables And Printing
\t* 6: Strings And Text
\t* 7: More Printing
\t* 8: Printing, Printing
\t* 9: Printing, Printing, Printing
\t* 10: What Was That
        """
        ExerciseB = raw_input("> ")
        Beginner.run(ExerciseB)
        
    # 'if' difficulty is 'Intermediate':
    elif Difficulty == "Intermediate":
        print "Please select your exercise"
        print """
\t* Intro:
\t* 1: 
\t* 2: 
\t* 3: 
\t* 4: 
\t* 5: 
\t* 6: 
\t* 7: 
\t* 8: 
\t* 9: 
\t* 10: 
        """
        ExerciseI = raw_input("> ")
        Beginner.run(ExerciseI)
        
    # 'if' difficulty is 'Advanced':
    elif Difficulty == "Advanced":
        print "Please select your exercise"
        print """
\t* Intro:
\t* 1: 
\t* 2: 
\t* 3: 
\t* 4: 
\t* 5: 
\t* 6: 
\t* 7: 
\t* 8: 
\t* 9:
\t* 10: 
        """
        ExerciseA = raw_input("> ")
        Beginner.run(ExerciseA)
    
    # if no 'if' or 'elif' statments are run, run this:
    else:
        print "Invalid"
        # repeat to beggining of program
        Program = True
