
"""
this involves creating a function to handle the game record.
for example ['4','-2','C', 'D', '+']
if the result is 4 you add it to the scores list.
if record is -2 you add to scores list
if record is C you remove the last added record to the score list,,remove -2.
if record is D you multiply the last added record to the list by 2 ie. 4 * 2 and add the result to the scores list.
if record is + you add 5 to the last added record to the list and add the result to the scores list.
you should return the total scores
"""

def  game_record(records):
    stack = []
    total_scores = 0
    
    for record in records:
        if record.isdigit():
            stack.append(int(record))
        
        elif record == 'C':
            if stack:
                stack.pop()
            
        elif record == 'D':
            if stack:
                last_item = stack[-1]
                multiplied_item = last_item * 2
                stack.append(multiplied_item)
                
        elif record == '+':
            if stack:
                last_item = stack[-1]
                added_item = last_item + 5
                stack.append(added_item)
    
   
    total_scores = sum(stack)
        
    return total_scores
    
new_record = ['5','3','C','D','10','+']
print(game_record(new_record)) # Output :40