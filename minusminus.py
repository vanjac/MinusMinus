import sys
program = sys.stdin.read(None)
stack = [ ]
returnStack = [ ]
idCharFlag = False
counter = 0
variables = [ ] # tuple (hash, value)
namespaces = [ ] # starting indices
memory = [ ]
memoryStart = -65536.0
while counter < len(program):
    c = program[counter]
    setIdCharFlag = False
    if c == ')':
        startIndex = len(stack) - 1
        while startIndex >= 0:
            if stack[startIndex] == ord('(') - ord('0'):
                break
            startIndex -= 1
        args = list(stack[startIndex+1:])
        del stack[startIndex:]
        arg1 = args.pop(0)
        op = chr(int(args.pop(0)) + ord('0'))
        if op == '!':
            namespaces.append(len(variables))
            stack += args
            returnStack.append(counter)
            counter = int(arg1) - 1
        else:
            arg2 = args[0]
        if op == '+':
            stack.append(arg1 + arg2)
        elif op == '-':
            stack.append(arg1 - arg2)
        elif op == '*':
            stack.append(arg1 * arg2)
        elif op == '/':
            stack.append(arg1 / arg2)
        elif op == '%':
            stack.append(arg1 % arg2)
        elif op == '?':
            stack.append(args[0] if arg1 != 0 else args[1])
        elif op == ':':
            stack.append(arg2)
            if arg1 < 0:
                memory[int(arg1 - memoryStart)] = arg2
            else:
                varI = len(variables) - 1
                while varI >= 0:
                    if variables[varI][0] == arg1:
                        variables[varI] = (arg1, arg2)
                        break
                    varI -= 1
    elif c == ';':
        del stack[-1]
    elif c == '|':
        stack.append(int(stack.pop() < 0))
    elif c == '$':
        variables.append((stack[-1], stack.pop(-2)))
    elif c == '^':
        addr = stack.pop()
        if addr < 0:
            stack.append(memory[int(addr - memoryStart)])
        else:
            for variable in reversed(variables):
                if variable[0] == addr:
                    stack.append(variable[1])
                    break
    elif c == '[':
        stack.append(float(counter + 1))
        depth = 1
        while counter < len(program) and depth != 0:
            counter += 1
            if program[counter] == '[':
                depth += 1
            elif program[counter] == ']':
                depth -= 1
    elif c == ']':
        counter = returnStack.pop()
        del variables[namespaces.pop() :]
    elif c == '#':
        stack.append(len(memory) + memoryStart)
        memory += [0.0 for i in range(0,int(stack.pop(-2)))]
    elif c != ' ' and c != '\n' and c != '\t':
        if not idCharFlag:
            stack.append(0.0)
        stack[-1] = stack[-1] * 10 + ord(c) - ord('0')
        setIdCharFlag = True
    idCharFlag = setIdCharFlag
    counter += 1
print(stack)
