s = "2[abc]3[cd]ef"
def decodeString(s):
    stack = []  # Stack to store characters and numbers
    current_string = ""  # Holds the current decoded string
    current_number = 0  # Stores the number before '['
    
    for char in s:
        if char.isdigit():
            print("--: ",int(char))
            current_number = current_number * 10 + int(char)  # Handle multi-digit numbers
        elif char == '[':
            # Push the current string and number to the stack and reset them
            stack.append((current_string, current_number))
            current_string = ""
            current_number = 0
        elif char == ']':
            # Pop from stack, decode the string
            prev_string, num = stack.pop()
            current_string = prev_string + num * current_string
        else:
            # Append normal characters
            current_string += char

    return current_string

             
            
                
    
print(decodeString(s))