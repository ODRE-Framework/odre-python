from datetime import datetime, timezone
import requests

# Casters

def cast_date(node):
    return datetime.strptime(node, "%Y-%m-%d")

def cast_time(node):
    return datetime.strptime(node, "%H:%M:%S")

def cast_datetime(node):
    return datetime.strptime(node, "%Y-%m-%dT%H-%M-%S")

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

def odrl_neg(operand1, operand2):
    return operand1 != operand2

# Functions

def odrl_dateTime():
    return datetime.now()


# Actions



'''
    EXTENSIONS
'''

''' Time extension'''
# Operands
def time_time():
    return cast_time(datetime.now().strftime('%H:%M:%S'))

def time_date():
    return cast_date(datetime.now().strftime('%Y-%m-%d'))

#Operator
def time_between(operand1, operand2):
    if operand1 <= operand2:
        return operand1 <= datetime.now() <= operand2
    else:
        return datetime.now() >= operand1 or datetime.now() <= operand2

''' Dummy extension '''

# Action
def demo_dummyRead():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    return response.json()
