import imp
import sys
from io import StringIO, TextIOWrapper
from StringIO import StringIO as old_StringIO

entry_point = imp.load_source("sub_format", "target_script/hs-sub-formatter/sub_format.py")


class UnclosableStringIO(StringIO):
    def __init__(self, *args, **kwargs):
        StringIO.__init__(self, *args, **kwargs)

    def close(self):
        # Seriously, if I can't call .getvalue() after it's closed then what is the fucking
        # point of using it as some sort of destination buffer.
        pass

def execute(input):
    output = UnclosableStringIO()
    stdout = old_StringIO()

    try:
        old_stdout = sys.stdout
        sys.stdout = stdout

        entry_point.main(['unused', 'unused', '--no-resolve', '--print-headers'],
            StringIO(input),
            output
        )
    except:
        raise
    finally:
        sys.stdout = old_stdout

    return stdout.getvalue(), output.getvalue()

