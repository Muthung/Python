def simplify_path(path):
    components = path.split('/')
    stack = []
    
    for component in components:
        if component == '.' or not component:
            continue
        elif component == '..':
            if stack:
                stack.pop()
            else:
                stack.append(component)
    return '/' + '/'.join(stack)