import re

debug = False
            
class StripDict(dict):

        def __getitem__(self, key):
            return ''
            
strip = StripDict()

def make_command(instring, rounds=3, roundn=1, **invars):    
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
            return make_command(outstr, rounds=rounds, roundn=roundn+1, **invars)
        return outstr
    else:
        return instring

def run_command(command):
    parts = re.finditer("\:\(.*?(?=\)\=)\)\=", command)
    
    lastspan = 0        
    outstr = ""
    
    if parts:
        for match in parts:
            span = list(match.span())    
            span[0] -= (span[1]-2) - (span[0]+2)
            outstr += command[lastspan:span[0]]
            lastspan = span[1]
        outstr += command[lastspan:]
    else:
        return command

    return outstr    
    
def make_dep_cmd(TOOL, env):
    return make_command(env['%sDEP' % TOOL], TOOL=TOOL, **env)
    
def make_compile_cmd(TOOL, env):
    return make_command("%(%(TOOL)s)s %(%(TOOL)sFLAGS)s %(%(TOOL)s_DEPFLAGS)s %(%(TOOL)s_C)s %(%(TOOL)s_O)s %(SOURCE)s", TOOL=TOOL, **env)

class MagPy(object):
    def __init__(self, deps=[], compilers=[], env={}, debug=False):
        self.debug = debug
        self.env = env
        self.tool_cmds = {}
        for tool in deps:
            self.tool_cmds['%sDEP' % tool] = make_dep_cmd(tool, env)
        for tool in compilers:
            self.tool_cmds[tool] = make_compile_cmd(tool, env)
        if self.debug:
            for k, v in self.tool_cmds.items():
                print '%s: %s' % (k,v)
    
    def compile(self, sources, fmatch, farch, compiler):
        sre = re.compile(fmatch)
        for source in sources:
            match  = sre.match(source)
            if match:
                res = match.groupdict()
                res.update({'ARCHIVE': farch % res, 'SOURCE': source})
                compile_cmd = make_command(self.tool_cmds[compiler], **res)
                if self.debug:
                    print compile_cmd
                
    def link_exe(self, sources,  library):
        link_command = make_command("%(LD)s %(LDFLAGS)s %(LDEXEFLAGS)s %(LD_O)s%(EXESUF)s %(SOURCE)s %(ELIBS)s", ARCHIVE=library, SOURCE=' '.join(sources), **self.env)
        if self.debug:
            print link_command
        
