from rdflib import Graph
from pyodre.python_interpreter import PythonInterpreter
from pyodre.interpreters import Interpreter
from jinja2 import Template
import logging
from pyodre.context import get_odrl_context

logger = logging.getLogger(__name__)


class ODRE:
    def __init__(self, debug=False):
        if debug:
            logger.setLevel(logging.DEBUG)
        self.__interpreter = PythonInterpreter()

    def set_interpreter(self, interpreter):
        if isinstance(interpreter, Interpreter):
            self.__interpreter = interpreter
            return self
        else:
            raise Exception("Provided interpreter is not a valid implementation, extend the class Interpreter from "
                            "interpreters")

    def set_debug(self, debug):
        self.__debug = debug
        return self

    def _rules(self, graph):
        rules_query = """
        SELECT DISTINCT ?rule_id WHERE {
            ?policy ?rule_relation  ?rule_id . 
            VALUES ?rule_relation { 
              <http://www.w3.org/ns/odrl/2/permission> 
              <http://www.w3.org/ns/odrl/2/obligation> 
              <http://www.w3.org/ns/odrl/2/prohibition> 
            } .
        }"""
        return [str(row.rule_id.n3()) for row in graph.query(rules_query)]

    def _constraints(self, rule_id, graph):
        rules_query = """
            SELECT DISTINCT ?operator ?left_operand ?right_operand WHERE {
                  """ + rule_id + """ <http://www.w3.org/ns/odrl/2/operator>  ?operator;
                    <http://www.w3.org/ns/odrl/2/leftOperand> ?left_operand ;
                    <http://www.w3.org/ns/odrl/2/rightOperand> ?right_operand .
    
            }"""
        return [(str(row.operator), row.left_operand, row.right_operand) for row in graph.query(rules_query)]

    def _action(self, rule_id, graph):
        rules_query = """
        SELECT DISTINCT ?action WHERE {
            """ + rule_id + """ <http://www.w3.org/ns/odrl/2/action>  ?action . 
        }"""
        return [str(row.action) for row in graph.query(rules_query)][0]

    def enforce(self, policy, format='json-ld', interpolations={}):
        templated_policy = Template(policy)
        logging.debug("Provided interpolations: ", interpolations)
        for templated_name, value in interpolations.items():
            templated_policy.globals[templated_name] = value
        interpolated_policy = templated_policy.render()
        logging.debug("Interpolated policy: ", interpolated_policy)
        # TODO: improve odrl context cache
        interpolated_policy = interpolated_policy.replace("\"http://www.w3.org/ns/odrl.jsonld\"", get_odrl_context())
        # DONE: solve template and interpolation
        descriptive_policy = Graph().parse(data=interpolated_policy, format=format)
        usage_decision = {}
        for rule_id in self._rules(descriptive_policy):
            constraints_set = self._constraints(rule_id, descriptive_policy)
            interpretable_policy = self.__interpreter.transform(constraints_set)
            decision = self.__interpreter.evaluate(interpretable_policy)
            logging.debug("Interpretable policy:", interpretable_policy, " decision: ", decision)
            if decision:
                descriptive_action = self._action(rule_id, descriptive_policy)
                interpretable_action = self.__interpreter.supports(descriptive_action)
                action_result = interpretable_action
                logging.debug("Action: ", descriptive_action, " supported: ", interpretable_action)
                if interpretable_action:
                    action_result = self.__interpreter.evaluate(interpretable_action)
                usage_decision[descriptive_action] = action_result
        logging.debug("Usage decisions: ", usage_decision)
        return usage_decision


