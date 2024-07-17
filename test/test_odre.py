from pyodre.odre import ODRE
import unittest

if __name__ == '__main__':
    unittest.main()


from pyodre.python_interpreter import PythonInterpreter


policy = """
{
    "@context": "http://www.w3.org/ns/odrl.jsonld",
    "@type": "Offer",
    "uid": "http://example.com/policy:6163",
    "profile": "http://example.com/odrl:profile:10",
    "permission": [{
       "target": "http://example.com/document:1234",
       "assigner": "http://example.com/org:616",
       "action": "distribute",
       "constraint": [{
           "leftOperand": "dateTime",
           "operator": "lt",
           "rightOperand":  { "@value": "2025-01-01", "@type": "xsd:date" }
       },{
           "leftOperand": { "@value": "{{retrieve_token()}}" , "@type": "xsd:string" },
           "operator": "eq",
           "rightOperand":  { "@value": "{{token}}", "@type": "xsd:string" }
       }]
   }]
}
"""

def get_token():
    return "AAA"

policy_constant_neq = """
{
    "@context": "http://www.w3.org/ns/odrl.jsonld",
    "@type": "Offer",
    "uid": "http://example.com/policy:6163",
    "profile": "http://example.com/odrl:profile:10",
    "permission": [{
       "target": "http://example.com/document:1234",
       "assigner": "http://example.com/org:616",
       "action": "read",
       "constraint": [{
           "leftOperand": { "@value": "2024-01-01", "@type": "xsd:date" },
           "operator": "neq",
           "rightOperand":  { "@value": "2025-01-01", "@type": "xsd:date" }
       }]
   }]
}
"""

policy_extension_operator = """
{
    "@context": ["http://www.w3.org/ns/odrl.jsonld",{"odreT":"https://w3id.org/def/odre-time#"}],
    "@type": "Offer",
    "uid": "https://helio.auroral.linkeddata.es/policy/2",
    "permission": [{
       "target": "https://helio.auroral.linkeddata.es/api/luminosity/data",
       "action": "read",
       "constraint": [{
           "leftOperand": { "@value": "06:55:00", "@type": "xsd:date" },
           "operator": "odreT:betweenTimes",
           "rightOperand":  { "@value": "23:55:00", "@type": "xsd:date" }
       }]
   }]
}
"""

policy_extension = """
{
    "@context": ["http://www.w3.org/ns/odrl.jsonld",{"odreT":"https://w3id.org/def/odre-time#"}],
    "@type": "Offer",
    "uid": "https://helio.auroral.linkeddata.es/policy/2",
    "permission": [{
       "target": "https://helio.auroral.linkeddata.es/api/luminosity/data",
       "action": "odreT:readDummy",
       "constraint": [{
           "leftOperand": { "@value": "06:55:00", "@type": "xsd:date" },
           "operator": "odreT:betweenTimes",
           "rightOperand":  { "@value": "23:55:00", "@type": "xsd:date" }
       }]
   }]
}
"""

class TestODRE(unittest.TestCase):
    """Test cases for the ODRE class."""

    def test_interpret(self):
        ''' Checks lt function '''
        usage_decision = ODRE().enforce(policy, interpolations={'token': 'AAA', 'retrieve_token': get_token})
        self.assertIsNotNone(usage_decision)
        self.assertEqual(str(usage_decision), "{'http://www.w3.org/ns/odrl/2/distribute': 'distribution action was executed'}")

    def test_neq(self):
        ''' Checks neq function '''
        usage_decision_constant_neq = ODRE().enforce(policy_constant_neq)
        self.assertIsNotNone(usage_decision_constant_neq)
        self.assertEqual(str(usage_decision_constant_neq), "{'http://www.w3.org/ns/odrl/2/read': 'read action was executed'}")

    def test_extension_operator(self):
        ''' Checks neq function '''
        usage_decision_constant_neq = ODRE().enforce(policy_extension_operator)
        self.assertIsNotNone(usage_decision_constant_neq)
        self.assertEqual(str(usage_decision_constant_neq), "{'http://www.w3.org/ns/odrl/2/read': 'read action was executed'}")