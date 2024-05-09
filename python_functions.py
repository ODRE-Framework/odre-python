from datetime import datetime

# Casters

def cast_date(node):
    return datetime.strptime(node, "%Y-%m-%d")

def cast_time(node):
    return datetime.strptime(node, "%Y-%m-%d")

def cast_datetime(node):
    return datetime.strptime(node, "%Y-%m-%d")

def cast_string(node):
    return str(node)

def cast_float(node):
    return float(node)

def cast_double(node):
    return float(node)

def cast_integer(node):
    return int(node)

# Operands

def odrl_eq(operand1, operand2):
    return operand1 == operand2

def odrl_lt(operand1, operand2):
    return operand1 < operand2

def odrl_gt(operand1, operand2):
    return operand1 > operand2

def odrl_lteq(operand1, operand2):
    return operand1 <= operand2

def odrl_gteq(operand1, operand2):
    return operand1 >= operand2

def odrl_neq(operand1, operand2):
    return operand1 != operand2

# Functions

def odrl_dateTime():
    return datetime.now()

def odrl_distribute():
    print("on distribution")