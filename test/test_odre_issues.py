from pyodre.odre import ODRE
import unittest
from datetime import date

POLICIES_DIR = "./policices/github_issues/"

def read_file(dir):
    f = open(dir, "r")
    content = f.read()
    f.close()
    return content

def enforce(policy, name, interpolations={}):
    return ODRE().enforce(policy, interpolations=interpolations)


class TestIssues(unittest.TestCase):
    """Tests for issues opened in https://github.com/ODRE-Framework/odre-framework/issues?q=is%3Aissue+is%3Aclosed."""

    def test_issue_1(self):
        policy = read_file(POLICIES_DIR+"issue1-policy.json")
        current_date = str(date.today())
        policy = policy.replace("#REPLACE#", current_date)
        print(policy)
        usage_decision = enforce(policy, "constant_lt")
        print(usage_decision)
        self.assertIsNotNone(usage_decision)
        self.assertTrue("http://www.w3.org/ns/odrl/2/distribute" in usage_decision.keys())


if __name__ == '__main__':
    unittest.main(verbosity=2)
