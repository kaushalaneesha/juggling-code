def ispar(x):
    stack = []
    for char in x:
        match char:
            case '[' | '{' | '(':
                stack.append(char)
            case ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            case '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            case ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
    if len(stack) == 0:
        return True
    return False

print(ispar('[]{}['))