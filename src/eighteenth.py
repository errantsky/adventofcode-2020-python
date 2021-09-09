def shunting_yard(inp, prec_dict):
    operators = ["+", "*"]
    output_queue = []
    operator_stack = []

    for token in inp:
        try:
            num = int(token)
            output_queue.append(num)
        except ValueError:
            if token in operators:
                while (
                    len(operator_stack) != 0
                    and (operator_stack[-1] == "+" or operator_stack[-1] == "*")
                    and (prec_dict.get(operator_stack[-1]) > prec_dict.get(token))
                ):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                # potential empty array
                while operator_stack[-1] != "(":
                    output_queue.append(operator_stack.pop())
                if operator_stack[-1] == "(":
                    operator_stack.pop()
    if len(operator_stack) != 0:
        while len(operator_stack) != 0:
            output_queue.append(operator_stack.pop())

    return output_queue


def eval_rpn(inp):
    num_count = 0
    while len(inp) != 1:
        for i in range(len(inp)):
            if inp[i] in ("+", "*"):
                lhs = inp[i - 2]
                rhs = inp[i - 1]
                if inp[i] == "+":
                    res = lhs + rhs
                else:
                    res = lhs * rhs
                inp[i] = res
                inp.pop(i - 1)
                inp.pop(i - 2)
                break
    return inp[0]


precedence_dict = {"+": 1, "*": 0}
acc = 0
with open("input/in18.txt") as f:
    for line in f:
        line = line.rstrip()
        rpn = shunting_yard(line, precedence_dict)
        print(rpn)
        res = eval_rpn(rpn)
        acc += res

print(acc)
