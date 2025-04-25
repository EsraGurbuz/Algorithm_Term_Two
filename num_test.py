import sys
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
def day_num(num):
    if days[num]:
        return int
    else:
        return
    
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
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(days_name(3)) == 3)
    test(days_name(day_num("Thursday")) == "Thursday")

test_suite()