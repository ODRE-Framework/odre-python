from pyodre.interpreters import Interpreter
import pyodre.python_functions
from pyodre.python_functions import *
from rdflib.term import Literal


class PythonInterpreter(Interpreter):

    def __init__(self):
        self.__prefixes_mappings = {"odrl_": "http://www.w3.org/ns/odrl/2/",
                                    "cast_": "http://www.w3.org/2001/XMLSchema#",
                                    "time_": "https://w3id.org/def/odre-time#" }

    def get_prefixes_mappings(self):
        return self.__prefixes_mappings

    def set_prefixes_mappings(self, new_prefixes):
        self.__prefixes_mappings = new_prefixes

    def add_prefix_mapping(self, prefix, uri):
        self.__prefixes_mappings[prefix] = uri

    def transform(self, constraints_set):
        concatenation_token = " and "
        interpretable_policy = ""
        for operator, left_operand, right_operand in constraints_set:
            interpretable_policy += self.__transform_constraint(operator, left_operand, right_operand)
            interpretable_policy += concatenation_token
        last_index = len(interpretable_policy) - len(concatenation_token)
        return interpretable_policy[:last_index]

    def __transform_constraint(self, operator_node, left_operand_node, right_operand_node):
        interpretable_operator = self.__interpreted_function_mappings(operator_node)
        interpretable_left = self.__transform_node(left_operand_node)
        interpretable_right = self.__transform_node(right_operand_node)
        return str(interpretable_operator) + "(" + str(interpretable_left) + ", " + str(interpretable_right) + ")"

    def __transform_node(self, node):
        if isinstance(node, Literal):
            interpretable_datatype = self.__interpreted_function_mappings(node.datatype)
            return interpretable_datatype + "(\"" + str(node.value) + "\")"
        return self.__interpreted_function_mappings(str(node)) + "()"

    def __interpreted_function_mappings(self, value):
        interpretable_node = None
        for prefix_mapping, uri_mapping in self.__prefixes_mappings.items():
            if uri_mapping in value:
                interpretable_node = value.replace(uri_mapping, prefix_mapping)
                break
        if interpretable_node is None:
            raise Exception(
                "Unknown URI, please provide a prefix mapping for this URI, e.g., '{ \"odrl_\" : "
                "\"http://www.w3.org/ns/odrl/2/\" }'")
        return interpretable_node

    def evaluate(self, expression):
        return eval(expression)

    def supports(self, action):
        interpretable_action = self.__interpreted_function_mappings(action)
        if hasattr(pyodre.python_functions, interpretable_action):
            return interpretable_action+"()"
        return None
