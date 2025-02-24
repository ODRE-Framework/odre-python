from pyodre.odre import ODRE
import unittest
import time
import pandas as pd

POLICIES_DIR = "./policices/basic-experiments/"
EXPERIMENTAL_MODE = True
iterations = 10
dict = {}


def read_file(dir):
    f = open(dir, "r")
    content = f.read()
    f.close()
    return content

def enforce(policy, name, interpolations={}):
    global dict, EXPERIMENTAL_MODE

    name = "test_" + name
    usage_decision = {}
    if EXPERIMENTAL_MODE:
        for i in range(iterations):
            start = time.time()
            usage_decision = ODRE().enforce(policy, interpolations=interpolations)
            end = time.time() - start
            if name in dict:
                dict[name] = dict[name] + [end]
            else:
                dict[name] = [end]
    else:
        usage_decision = ODRE().enforce(policy, interpolations=interpolations)
    df = pd.DataFrame(dict)
    df.to_csv(POLICIES_DIR + 'running.csv', header=True)
    return usage_decision

def function_get_time():
    return "23:55:00"

class TestODRE(unittest.TestCase):
    """Tests for basic cases using ODRE class."""

    def test_policy_constant_lt(self):
        policy = read_file(POLICIES_DIR+"1-policy_constant_lt.json")
        usage_decision = enforce(policy, "constant_lt")
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys())

    def test_policy_constant_lteq(self):
        policy = read_file(POLICIES_DIR + "2-policy_constant_lteq.json")
        usage_decision = enforce(policy,"constant_lteq")
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys())

    def test_policy_constant_eq(self):
        policy = read_file(POLICIES_DIR + "3-policy_constant_eq.json")
        usage_decision = enforce(policy, "constant_eq")
        self.assertIsNotNone(usage_decision)
        self.assertTrue(len(usage_decision.keys()) == 0)

    def test_policy_constant_neq(self):
        policy = read_file(POLICIES_DIR + "4-policy_constant_neq.json")
        usage_decision = enforce(policy,"constant_neq")
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys())

    def test_policy_constant_gteq(self):
        policy = read_file(POLICIES_DIR + "5-policy_constant_gteq.json")
        usage_decision = enforce(policy,"constant_gteq")
        self.assertIsNotNone(usage_decision)
        self.assertTrue(len(usage_decision.keys()) == 0)

    def test_policy_constant_gt(self):
        policy = read_file(POLICIES_DIR + "6-policy_constant_gt.json")
        usage_decision = enforce(policy, "constant_gt")
        self.assertIsNotNone(usage_decision)
        self.assertTrue(len(usage_decision.keys()) == 0)

    def test_policy_datetime_lt(self):
        policy = read_file(POLICIES_DIR + "7-policy_datetime_lt.json")
        usage_decision = enforce(policy, "datetime_lt")
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys())

    def test_policy_datetime_lteq(self):
        policy = read_file(POLICIES_DIR + "8-policy_datetime_lteq.json")
        usage_decision = enforce(policy, "datetime_lteq")
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys())

    def test_policy_datetime_eq(self):
        policy = read_file(POLICIES_DIR + "9-policy_datetime_eq.json")
        usage_decision = enforce(policy, "datetime_eq")
        self.assertIsNotNone(usage_decision)
        self.assertTrue(len(usage_decision.keys()) == 0)

    def test_policy_datetime_neq(self):
        policy = read_file(POLICIES_DIR + "10-policy_datetime_neq.json")
        usage_decision = enforce(policy, "datetime_neq")
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys())

    def test_policy_datetime_gteq(self):
        policy = read_file(POLICIES_DIR + "11-policy_datetime_gteq.json")
        usage_decision = enforce(policy, "datetime_gteq")
        self.assertIsNotNone(usage_decision)
        self.assertTrue(len(usage_decision.keys()) == 0)

    def test_policy_datetime_gt(self):
        policy = read_file(POLICIES_DIR + "12-policy_datetime_gt.json")
        usage_decision = enforce(policy, "datetime_gt")
        self.assertIsNotNone(usage_decision)
        self.assertTrue(len(usage_decision.keys()) == 0)

    def test_policy_extension_operand_lt(self):
        policy = read_file(POLICIES_DIR + "13-policy_extension_operand_lt.json")
        usage_decision = enforce(policy, "extension_operand_lt")
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys())

    def test_policy_extension_operand_lteq(self):
        policy = read_file(POLICIES_DIR + "14-policy_extension_operand_lteq.json")
        usage_decision = enforce(policy, "extension_operand_lteq")
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys() or len(usage_decision.keys()) == 0)

    def test_policy_extension_operand_eq(self):
        policy = read_file(POLICIES_DIR + "15-policy_extension_operand_eq.json")
        usage_decision = enforce(policy, "extension_operand_eq")
        self.assertIsNotNone(usage_decision)
        self.assertTrue(len(usage_decision.keys()) == 0)

    def test_policy_extension_operand_neq(self):
        policy = read_file(POLICIES_DIR + "16-policy_extension_operand_neq.json")
        usage_decision = enforce(policy, "extension_operand_neq")
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys())

    def test_policy_extension_operand_gteq(self):
        policy = read_file(POLICIES_DIR + "17-policy_extension_operand_gteq.json")
        usage_decision = enforce(policy, "extension_operand_gteq")
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys() or len(usage_decision.keys()) == 0)

    def test_policy_extension_operand_gt(self):
        policy = read_file(POLICIES_DIR + "18-policy_extension_operand_gt.json")
        usage_decision = enforce(policy, "extension_operand_gt")
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys() or len(usage_decision.keys()) == 0)

    def test_policy_extension_operator(self):
        policy = read_file(POLICIES_DIR + "19-policy_extension_operator.json")
        usage_decision = enforce(policy, "extension_operator")
        self.assertIsNotNone(usage_decision)
        self.assertTrue(len(usage_decision.keys()) > 0)

    def test_policy_extension_action(self):
        policy = read_file(POLICIES_DIR + "20-policy_extension_action.json")
        usage_decision = enforce(policy, "extension_action")
        self.assertIsNotNone(usage_decision)
        self.assertTrue(len(usage_decision.keys()) > 0)

    def test_policy_interpolation_variable_left_eq(self):
        policy = read_file(POLICIES_DIR + "21-jinja-policy_interpolation_variable_left_eq.json")
        usage_decision = enforce(policy, "interpolation_variable_left_eq", {'curre_time': '23:55:00'})
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys())

    def test_policy_interpolation_variable_right_eq(self):
        policy = read_file(POLICIES_DIR + "22-jinja-policy_interpolation_variable_right_eq.json")
        usage_decision = enforce(policy, "interpolation_variable_right_eq", {'curre_time': '23:55:00'})
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys())

    def test_policy_interpolation_function_left_eq(self):
        policy = read_file(POLICIES_DIR + "23-jinja-policy_interpolation_function_left_eq.json")
        usage_decision = enforce(policy, "interpolation_function_left_eq", {'get_time': function_get_time})
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys())

    def test_policy_interpolation_function_right_eq(self):
        policy = read_file(POLICIES_DIR + "24-jinja-policy_interpolation_function_right_eq.json")
        usage_decision = enforce(policy, "interpolation_function_right_eq", {'get_time': function_get_time})
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/read" in usage_decision.keys())


if __name__ == '__main__':
    unittest.main(verbosity=2)
