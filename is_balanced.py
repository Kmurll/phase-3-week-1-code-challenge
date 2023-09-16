def is_balanced(expression):
    stack = []  # Initialize an empty stack to store opening brackets

    # Define a mapping of opening brackets to their corresponding closing brackets
    bracket_mapping = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the expression
    for char in expression:
        if char in bracket_mapping.values():
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
        elif char in bracket_mapping.keys():
            # If it's a closing bracket, check if the stack is empty
            # or if the top of the stack matches the corresponding opening bracket
            if not stack or stack.pop() != bracket_mapping[char]:
                return False

    # After iterating through the expression, the stack should be empty if it's balanced
    return not stack

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
expression3 = "[({})]"
expression4 = "{[()]}"
expression5 = "}"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
print(is_balanced(expression3))  # Output: True
print(is_balanced(expression4))  # Output: True
print(is_balanced(expression5))  # Output: False

