import re
class VDF:

    TYPEEX = { #RE's to handle type conversion
    'INT': re.compile(r'^\-?\d+$'),
    'FLOAT': re.compile(r'^\-?\d+\.\d+$'),
    'BOOLEAN': re.compile(r'^(true|false)$', re.IGNORECASE),
    }

    def __init__(self,options=None):
        '''
        :param options: (dict)  
            :types bool: (True) detect and convert values into data types
            :arrayify bool: (True) convert repeated keys into lists to retain them
            :conditionals str/list[str]: (None) conditional blocks e.g. "key" "value" [$DEBUG] will only be included if "DEBUG" is added to conditionals, default None=includeall
            '''
        #setup options
        if options is None:
            options = {}
        elif(isinstance(options,bool)):
            options={"types":options}
        self.options = {
            "types":options.get("types",True),
            "arrayify":options.get("arrayify",True),
            "conditionals":options.get("conditionals")
        }
        if(isinstance(self.options["conditionals"],str)):
            self.options["conditionals"]=[self.options["conditionals"]]

    def parseVdf(self,text):
        '''Converts a text representation of vdf file into a dictionary
        :param text: (str) vdf text
        
        :returns: (dict) representation of vdf file
        '''
        if not isinstance(text, str):
            raise TypeError('Expected parameter to be string')

        lines = text.splitlines()
        if(lines[0].startswith('\ufeff')):#remove BOM 
            lines[0]=lines[0][1:]
        obj = {}
        stack = [obj]
        expect_bracket = False

        re_kv = re.compile(
            r'^[ \t]*'
            r'("((?:\\.|[^\\"])+)"|([a-zA-Z0-9\-_]+))'
            r'([ \t]*('
            r'"((?:\\.|[^\\"])*)("?|$)'
            r'|([a-zA-Z0-9\-_\.]+)'
            r'))?'
            r'(?:[ \t]*\[(\!?[$][A-Z0-9]+(?:(?:[\|]{2}|[\&]{2})\!?[$][A-Z0-9]+)*)\])?'
        )

        i = -1
        j = len(lines)
        sublines = []
        odd = False
        def getNextLine():
            nonlocal odd
            nonlocal sublines
            nonlocal i

            if sublines:
                _subline = sublines.pop(0)
                if not odd:
                    _subline = _subline.strip()
                return _subline

            i += 1
            while i < len(lines):
                _line = lines[i].strip()
                if _line == '' or _line[0] == '/':
                    i += 1
                    continue  # Skip empty lines and comments
                else:
                    break

            if(i>=len(lines)):
                return None

            comment_slash_pos = -1

            l=0
            __line=_line
            while(l<len(_line)):
                char = _line[l]
                if(char =='"'):
                    if(l==0 or _line[l-1]!='\\'):
                        odd= not odd
                elif(char =='/' and not odd):
                    comment_slash_pos=l
                    l+=1
                    break
                elif(char=='{' and not odd):
                    __line = _line[:l] + "\n{\n" + _line[l+1:]
                elif(char=='}' and not odd):
                    __line = _line[:l]+"\n}\n" + _line[l+1:]
                l+=1
            _line=__line

            if comment_slash_pos > -1:
                _line = _line[:comment_slash_pos]

            sublines = _line.split("\n")
            return getNextLine()

        while True:
            line = getNextLine()
            if line is None:
                break
            if line == "" or line[0] == "/":
                continue

            if line[0] == "{":
                #print(f"Opening block: {stack[-1]}\n")
                expect_bracket = False
                continue
            if expect_bracket:
                raise SyntaxError(f"Invalid syntax on line {i + 1} (expected opening bracket, empty unquoted values are not allowed):\n{line}")

            if line[0] == "}":
                #print(f"Closing block: {stack[-1]}\n")
                if(len(stack)>1 and isinstance(stack[-2], list)):
                    stack.pop()
                stack.pop()
                continue

            while True:
                m = re_kv.match(line)

                if m is None:
                    raise SyntaxError(f"Invalid syntax on line {i + 1}:\n{line}")

                key = m.group(2) or m.group(3)
                val = m.group(6) if m.group(6) is not None else m.group(8)#val = m.group(6) or m.group(8)
                six = m.group(6)
                eight = m.group(8)

                if val is None:
                    if key not in stack[-1]:
                        stack[-1][key] = {}
                        stack.append(stack[-1][key])
                    elif isinstance(stack[-1][key], dict):
                        if self.options["arrayify"]:
                            stack[-1][key] = [stack[-1][key], {}]
                            stack.append(stack[-1][key])
                            stack.append(stack[-1][1])
                        else:
                            stack.append(stack[-1][key])
                    elif isinstance(stack[-1][key], list):
                        if not self.options["arrayify"]:
                            raise Exception('Code block should never be reached with arrayify set to false')
                        stack.append(stack[-1][key])
                        stack[-1].append({})
                        stack.append(stack[-1][-1])
                    expect_bracket = True
                else:
                    if m.group(7) is None and m.group(8) is None:
                        if i + 1 >= j:
                            raise SyntaxError('Unclosed quotes at end of file')
                        line += "\n" + getNextLine()
                        continue

                    if self.options["conditionals"] and m.group(9):
                        conditionals = m.group(9)
                        single_cond_regex = re.compile(r'(\|\||&&)?(!)?[$]([A-Z0-9]+)')
                        ok = False

                        while conditionals:
                            d = single_cond_regex.match(conditionals)
                            if not d or not d.group(3):
                                raise SyntaxError('Encountered incorrect conditional: ' + conditionals)

                            conditionals = conditionals.replace(d.group(0), '').strip()
                            op = d.group(1)
                            nt = d.group(2) == "!" if d.group(2) else False
                            cond = d.group(3)
                            includes = cond in self.options["conditionals"]
                            _ok = not includes if nt else includes
                            if not op or op == "||":
                                ok = ok or _ok
                            else:
                                ok = ok and _ok

                        if not ok:
                            line = line.replace(m.group(0), "").strip()
                            if not line or line[0] == '/':
                                break
                            continue

                    if self.options["types"]:
                        if self.TYPEEX["INT"].match(val):
                            val = int(val)
                        elif self.TYPEEX["FLOAT"].match(val):
                            val = float(val)
                        elif self.TYPEEX["BOOLEAN"].match(val):
                            val = val.lower() == "true"

                    if stack[-1].get(key) is None:
                        stack[-1][key] = val
                    elif not isinstance(stack[-1][key], list):
                        if self.options["arrayify"]:
                            stack[-1][key] = [stack[-1][key], val]
                        else:
                            stack[-1][key] = val
                    elif isinstance(stack[-1][key], list):
                        if not self.options["arrayify"]:
                            raise Exception('Execution should never reach this block with arrayify false')
                        stack[-1][key].append(val)

                if expect_bracket:
                    break
                line = line.replace(m.group(0), "").strip()
                if not line or line[0] == '/':
                    break
                line = re.sub(r'^\s*\[\!?\$[A-Z0-9]+(?:(?:\|\||&&)\!?\$[A-Z0-9]+)*\]', "", line).strip()
                if not line or line[0] == '/':
                    break

        return obj

    def dump(self,vdf, indentLevel=0):
        '''Converts vdf dictionary back to vdf
        :param vdf: Parsed vdf dict
        :param indentLevel: Current level of indentation
        :return: A string representation of vdf file
        '''
        out=""
        lineIndent = '\t'*indentLevel
        if(type(vdf)==str):
            return out
        for key, value in vdf.items():
            if(isinstance(value,dict)):
                out+='{}"{}"\n'.format(lineIndent,key)
                out+='{}{{\n'.format(lineIndent)
                out+=self.dump(value,indentLevel+1)
                out+='{}}}\n'.format(lineIndent)

            elif(isinstance(value,list)):
                for v in value:
                    out+='{}"{}"\n'.format(lineIndent,key)
                    out+='{}{{\n'.format(lineIndent)
                    out+=self.dump(v, indentLevel+1)
                    out+='{}}}\n'.format(lineIndent)
            else:
                if(isinstance(value,bool)):
                    value = "true" if value else "false"
                out+='{}"{}"\t"{}"\n'.format(lineIndent,key,value)
        return out
