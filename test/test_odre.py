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

class TestODRE(unittest.TestCase):
    """Test cases for the ODRE class."""

    def test_interpret(self):
        
        ''' Checks lt function '''
        usage_decision = ODRE().enforce(policy, interpolations={'token': 'AAA', 'retrieve_token': get_token})
        self.assertIsNotNone(usage_decision)
        self.assertEqual(str(usage_decision), "{'http://www.w3.org/ns/odrl/2/distribute': True}")