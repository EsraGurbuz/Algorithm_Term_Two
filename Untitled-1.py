import sys
def turn_clockwise(way):
    if way == "N":
        return "E"
    elif way == "E":
        return "S"
    elif way == "S":
        return "W"
    elif way == "W":
        return "N"
    else:
        return 
    
    #FİREBASE

def test(did_pass):
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)

test_suite()