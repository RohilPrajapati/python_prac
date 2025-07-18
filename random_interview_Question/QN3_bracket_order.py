# 3. Write a function that checks if a sequence of brackets like: “{[({})]}” is valid or not.

def is_valid_bracket_sequence(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            pass
    
    return len(stack) == 0

if __name__ == '__main__':
    bracket =  "{[({})]}()}"
    result = is_valid_bracket_sequence(bracket)
    if result:
        print("Is Valid")
    else:
        print("Is not Valid")