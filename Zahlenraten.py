import random
a=random.randrange(12)

of=True

while of:
    x= input  ("Geben Sie eine zahl ein: ")
    if x< 0 or x > 13:
        print " Zahl ist außerhalb des Bereichs." 
    if x < a:
        print "zu niedrig"
    elif x == a:
        print "Super,das ist die richtige Zahl."
        of = False
    else:
        print "zu hoch"

# Die Schleife wird sooft wiederholt bis die richtige Zahl erreicht ist.
# richtige zahl löst das Ende aus.