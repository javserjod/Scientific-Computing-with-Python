""" INFORMATION
Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, 
and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. 
When the second argument is set to True, the answers should be displayed.


-------------------- RULES ------------------------
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
Numbers should be right-aligned.
There should be four spaces between each problem.
There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
"""

# Solution by Javier Serrano Jodral

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_ops = []
    operators = []
    second_ops = []

    for problem in problems:
        components = problem.split(' ')
        first_op = components[0]
        operator = components[1]
        second_op = components[2]
        
        # Input error checking -> raise corresponding Exception
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not first_op.isdigit() or not second_op.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(first_op)>4 or len(second_op)>4:
            return 'Error: Numbers cannot be more than four digits.'
        
        
        max_op_width = max(len(first_op), len(second_op))
        total_width = max_op_width + 2   # 2 = space + operator
        
        first_ops.append(first_op)
        operators.append(operator)
        second_ops.append(second_op)

    num_op = len(operators)

    # First line
    res = ''
    for problem in range(num_op):
        max_op_width = max(len(first_ops[problem]), len(second_ops[problem]))
        total_width = max_op_width + 2   # 2 = space + operator
        
        res += ' '*(total_width-len(first_ops[problem])) + first_ops[problem] 
        
        if problem < num_op-1:   # add spaces between problems if not last
            res += ' '*4

    # Second line
    res += '\n'
    for problem in range(num_op):
        max_op_width = max(len(first_ops[problem]), len(second_ops[problem]))
        total_width = max_op_width + 2   # 2 = space + operator
        
        res += operators[problem] + ' '*(max_op_width+1-len(second_ops[problem]))+ second_ops[problem]

        if problem < num_op-1:   # add spaces between problems if not last
            res += ' '*4
    
    # Dashed line
    res += '\n'
    for problem in range(num_op):
        max_op_width = max(len(first_ops[problem]), len(second_ops[problem]))
        total_width = max_op_width + 2   # 2 = space + operator
        
        res += '-'*total_width
        if problem < num_op-1:   # add spaces between problems if not last
            res += ' '*4

    # Results line
    if show_answers:
        res += '\n'
        for problem in range(num_op):
            max_op_width = max(len(first_ops[problem]), len(second_ops[problem]))
            total_width = max_op_width + 2   # 2 = space + operator
            
            if operators[problem] == '+':
                answer = str(int(first_ops[problem]) + int(second_ops[problem]))
            else:
                answer = str(int(first_ops[problem]) - int(second_ops[problem]))

            res +=  ' '*(total_width - len(answer)) + answer
            if problem < num_op-1:   # add spaces between problems if not last
                res += ' '*4


    problems = res
    return problems


mine = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)
sol = '   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028'

print(f'{repr(mine)}')
print(f'{repr(sol)}')

print('\n')
print(f'{(mine)}')
print('\n')
print(f'{(sol)}')