equations = []

while True:
    eq = input("Input an equation (or 'exit' / 'done' / 'good' to finish the program): ")

    if eq.lower() in ('exit', 'done', 'good'):
        break

    equations.append(eq)

line_number = 1

for eq in equations:
    print(f"Line {line_number}:")
    i = 0

    while i < len(eq):
        if eq[i].isnumeric():
            j = i
            while j < len(eq) and (eq[j].isnumeric() or eq[j].isalpha()):
                j += 1
            token = eq[i:j]
            if any(c.isalpha() for c in token):
                print(f"Unidentified token on Line {line_number}, Index {i+1} -> {token}")
            else:
                print(token, "-> Number")
            i = j
        elif eq[i] == "+":
            print("+ : Addition")
            i += 1
        elif eq[i] == ":":
            if eq[i + 1] == "=":
                print(":= : Assign")
                i += 2
            else:
                print(": : Assign")
                i += 1
        elif eq[i] == "=":
            if eq[i - 1] == ":":
                pass
            else:
                print("= : Assign")

            i += 1
        elif eq[i] == "-":
            print("- : Subtraction")
            i += 1
        elif eq[i] == "(":
            print("( : lparen")
            i += 1
        elif eq[i] == ")":
            print(") : rparen")
            i += 1
        elif eq[i] == "*":
            print("* : Multiplication")
            i += 1
        elif eq[i] == "/":
            if i + 1 < len(eq) and eq[i + 1] == "/":
                print("// : Comment")
                break
            else:
                print("/ : Division")
                i += 1
        elif eq[i].isalpha() or (eq[i].isalnum() and i > 0 and eq[i-1].isalpha()):
            j = i

            while j < len(eq) and (eq[j].isalnum() or eq[j] == '.'):
                j += 1

            print(f"{eq[i:j]} : id")
            i = j
        else:
            i += 1

    line_number += 1
