
def macro_TestMacro(macro, name=str, age=int):
    outmsg = 'Your name is %s, and your are %d years old.'
    outmsg = outmsg % (name, age)
    return macro.formatter.text(outmsg)

