import re

def validate_let(line):
    if not line.startswith("let"):
        return False
    return True

def validate_parentheses(value):
    count = 0
    for char in value:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

def validate_single_quotes(value):
    return value.startswith("'") and value.endswith("'")

def reescribir_archivo(input_text):
    lines = input_text.split("\n")
    variables = {}
    errors = []

    for line in lines:
        if not validate_let(line):
            errors.append(f"Error en la línea: {line}. La línea debe comenzar con 'let'")
            continue
        
        var_name, value = line[4:].split(" = ")
        
        if not validate_single_quotes(value):
            errors.append(f"Error en la línea: {line}. Los valores deben estar entre comillas simples.")
            continue
        
        value = value.strip("'")
        
        if not validate_parentheses(value):
            errors.append(f"Error en la línea: {line}. Los paréntesis no están balanceados.")
            continue
        
        variables[var_name] = value

    if errors:
        for error in errors:
            print(error)
        return None

    for var_name, value in variables.items():
        for dependent_var in variables:
            variables[dependent_var] = variables[dependent_var].replace(var_name, f"({value})")

    output_lines = []
    for var_name, value in variables.items():
        output_lines.append(f"let {var_name} = '{value}'")

    return "\n".join(output_lines)


def get_values_list(rewritten_text):
    lines = rewritten_text.split("\n")
    values_list = []

    for line in lines:
        if line.startswith("let"):
            _, value = line.split(" = ")
            value = value.strip("'")
            values_list.append(value)

    return values_list
