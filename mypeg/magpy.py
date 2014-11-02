import re

debug = False
            
class StripDict(dict):

        def __getitem__(self, key):
            return ''
            
strip = StripDict()

def loop_substitute(instring, rounds=3, roundn=1, invars={}):    
    partit = re.finditer("\%\(.*?(?!\%\()(?=\)s|)\)s", instring)
    outstr = ""
    lastspan = 0
    if partit:
        for match in partit:
            span = list(match.span())
            foundstr = instring[span[0]:span[1]]
            span[0] = span[0] + foundstr.rfind("%(")
            repstring = instring[span[0]:span[1]]
            try:
                repstring = repstring % invars
            except KeyError:
                pass
            outstr += instring[lastspan:span[0]] + repstring
            lastspan = span[1]
        outstr += instring[lastspan:]
        if roundn < rounds:
            return loop_substitute(outstr, rounds=rounds, roundn=roundn+1, invars=invars)
        return outstr
    
def make_dep_cmd(TOOL, env):
    return loop_substitute(env['%sDEP' % TOOL], invars=dict(env, TOOL=TOOL))
    
def make_compile_cmd(TOOL, env):
    return loop_substitute("%(%(TOOL)s)s %(%(TOOL)sFLAGS)s %(%(TOOL)s_DEPFLAGS)s %(%(TOOL)s_C)s %(%(TOOL)s_O)s %(SOURCE)s", invars=dict(env, TOOL=TOOL))
