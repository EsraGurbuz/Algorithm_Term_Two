import sys 
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
def days_name(num):
    if num >= 0 and num <= len(days):
        return days[num]
    else:
        return 
        

def test(did_pass):
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    test(days_name(3) == "Wednesday")
    test(days_name(6) == "Saturday")
    test(days_name(42) == None)

test_suite()