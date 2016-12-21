import fileinput
import sys
from pkg_resources import replace

def main():
    for line in fileinput.input():
        outline = fixline(line)
        sys.stdout.writelines([outline])

def fixline(aInLine):
    retval = aInline
    if "nonlocal" in retval:
        retval = ""
    retval = retval.replace("print", "xprint")
    retval = retval.replace("_g_val", "_g_val[0]")
    retval = retval.replace("_g_head", "_g_head[0]")
    return retval
    
if __name__ == "__main__":
    main()