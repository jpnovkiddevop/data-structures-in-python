#implement using stack

def infix_to_postfix(expression):
    
    #precedence dictionary
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} 
    
    #initialize an empty stack and empty postfix list
    stack = []
    postfix = []
    
    #split the expression
    tokens = expression.split()
    
    for token in tokens:
        if token.isalnum():
            postfix.append(token) #add operand
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()  # Discard the '('
        else: #handle operator
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(token, 0):
                postfix.append(stack.pop())
            stack.append(token)
    #append remaining operators to postfix list
    while stack:
        postfix.append(stack.pop())
  
    return ''.join(postfix)
    
if __name__ =="__main__":
    infix_expr = "a + (b * c )+ ( d / e + f ) * g"
    postfix_expr = infix_to_postfix(infix_expr)
    print("Infix Expression:", infix_expr)
    print("Postfix Expression:", postfix_expr)    

