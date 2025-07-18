"""
4. Given a string path, which is an absolute path (starting with /) for a file or directory in a Unix-style file
system, simplify it. The simplified canonical path should follow these rules:
● A single dot "." refers to the current directory.
● A double dot ".." refers to the parent directory.
● Multiple slashes '//' are treated as a single slash '/'.
● The simplified path should always start with a single slash '/'.
● There should be no trailing slash at the end unless it's the root /.
● You must resolve “.” and “..” properly.
Return the simplified canonical path as a string.
"""

# Example of input and out

# Input: "/home/"
# Output: "/home"

# Input: "/../"
# Output: "/"

# Input: "/home//foo/"
# Output: "/home/foo"

# Input: "/a/./b/../../c/"
# Output: "/c"

# learn and completed using ChatGPT

def simplify_path(path):
    parts = path.split('/')
    stack = []

    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return '/' + '/'.join(stack)

if __name__ == '__main__':
    relative_path = "/a/./b/../../c/home/rohil/../ram/project"
    result = simplify_path(relative_path)
    print(result)


