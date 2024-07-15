# ODRE Framework




## Quickstart

#### Install

```bash
pip install pyodre
```

#### Enforce ODRL policies

```python
from pyodre.odre import ODRE

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
       }]
   }]
}
"""
usage_decision = ODRE().enforce(policy)
print(usage_decision)
```

In the case a user wants to activate the DEBUG mode that shows the interpretable policies, the actions and the usage decision the following excerpt must be used. In addition, note that the interpreter can be modified

```python
usage_decision = ODRE().set_debug(True).set_interpreter(PythonInterpreter()).enforce(policy)
print(usage_decision)
```

#### Register new functions (descriptive + interpretable)
TBD

### Interpolation

The policy templating is based on the Jinja language, it can be used to pass data variables that are not hardcoded in the policy increasing its privacy or it can be used to pass python native functions so they can be expressed in the policy and invoked during the enforcement.

In the following example a variable `{{token}}` is expressed in the policy and, as left operand, the function `{{retrieve_token()}}` is used. Note that the value of both is passed to the `ODRE` object under the parameter `interpolations`

```python
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

usage_decision = ODRE().set_debug(True).enforce(policy, interpolations={'token' : 'AAA', 'retrieve_token' : get_token})
print(usage_decision)
```


## Supported features

### ODRL operantors

| Operators | Implementation status | # |
|--|--| -- |
| [eq](https://www.w3.org/TR/odrl-vocab/#term-eq) | supported  | &check; |
| [gt](https://www.w3.org/TR/odrl-vocab/#term-gt)  | supported  | &check; |
| [gteq](https://www.w3.org/TR/odrl-vocab/#term-gteq) | unsupported  | &check; |
| [lt](https://www.w3.org/TR/odrl-vocab/#term-lt)  | supported  | &check; |
| [lteq](https://www.w3.org/TR/odrl-vocab/#term-lteq)  | supported  | &check; |
| [neq](https://www.w3.org/TR/odrl-vocab/#term-neq)  | supported  | &check; |
| [hasPart](https://www.w3.org/TR/odrl-vocab/#term-hasPart) | unsupported  | &cross; |
| [isA](https://www.w3.org/TR/odrl-vocab/#term-isA) | unsupported  | &cross; |
| [isAllOf](https://www.w3.org/TR/odrl-vocab/#term-isAllOf) | unsupported  | &cross; |
| [isAnyOf](https://www.w3.org/TR/odrl-vocab/#term-isAnyOf) | unsupported  | &cross; |
| [isNoneOf](https://www.w3.org/TR/odrl-vocab/#term-isNoneOf) | unsupported  | &cross; |
| [isPartOf](https://www.w3.org/TR/odrl-vocab/#term-isPartOf) | unsupported  | &cross; |

### ODRL operands
* The available implemented [Left Operands](https://www.w3.org/TR/odrl-vocab/#term-LeftOperand) from those specified in the [ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/) are the following:

| Left Operands                                                                               | Implementation status | # |
|---------------------------------------------------------------------------------------------|--| -- |
| [absolutePosition](https://www.w3.org/TR/odrl-vocab/#term-absolutePosition)                 | unsupported | &cross; |
| [absoluteSize](https://www.w3.org/TR/odrl-vocab/#term-absoluteSize)                         | unsupported | &cross; |
| [absoluteSpatialPosition](https://www.w3.org/TR/odrl-vocab/#term-absoluteSpatialPosition)   | unsupported | &cross; |
| [absoluteTemporalPosition](https://www.w3.org/TR/odrl-vocab/#term-absoluteTemporalPosition) | unsupported | &cross; |
| [count](https://www.w3.org/TR/odrl-vocab/#term-count)                                       | unsupported | &cross; |
| [dateTime](https://www.w3.org/TR/odrl-vocab/#term-dateTime)                                 | unsupported | &cross; |
| [delayPeriod](https://www.w3.org/TR/odrl-vocab/#term-delayPeriod)                           | unsupported | &cross; |
| [deliveryChannel](https://www.w3.org/TR/odrl-vocab/#term-deliveryChannel)                   | unsupported | &cross; |
| [device](https://www.w3.org/TR/odrl-vocab/#term-device)                                     | unsupported | &cross; |
| [elapsedTime](https://www.w3.org/TR/odrl-vocab/#term-elapsedTime)                           | unsupported | &cross; |
| [event](https://www.w3.org/TR/odrl-vocab/#term-event)                                       | unsupported | &cross; |
| [fileFormat](https://www.w3.org/TR/odrl-vocab/#term-fileFormat)                             | unsupported | &cross; |
| [industry](https://www.w3.org/TR/odrl-vocab/#term-industry)                                 | unsupported | &cross; |
| [language](https://www.w3.org/TR/odrl-vocab/#term-language)                                 | unsupported | &cross; |
| [media](https://www.w3.org/TR/odrl-vocab/#term-media)                                       | unsupported | &cross; |
| [meteredTime](https://www.w3.org/TR/odrl-vocab/#term-meteredTime)                           | unsupported | &cross; |
| [payAmount](https://www.w3.org/TR/odrl-vocab/#term-payAmount)                               | unsupported | &cross; |
| [percentage](https://www.w3.org/TR/odrl-vocab/#term-percentage)                             | unsupported | &cross; |
| [product](https://www.w3.org/TR/odrl-vocab/#term-product)                                   | unsupported | &cross; |
| [purpose](https://www.w3.org/TR/odrl-vocab/#term-purpose)                                   | unsupported | &cross; |
| [recipient](https://www.w3.org/TR/odrl-vocab/#term-recipient)                               | unsupported | &cross; |
| [relativePosition](https://www.w3.org/TR/odrl-vocab/#term-relativePosition)                 | unsupported | &cross; |
| [relativeSize](https://www.w3.org/TR/odrl-vocab/#term-relativeSize)                         | unsupported | &cross; |
| [relativeSpatialPosition](https://www.w3.org/TR/odrl-vocab/#term-relativeSpatialPosition)   | unsupported | &cross; |
| [relativeTemporalPosition](https://www.w3.org/TR/odrl-vocab/#term-relativeTemporalPosition) | unsupported | &cross; |
| [resolution](https://www.w3.org/TR/odrl-vocab/#term-resolution)                             | unsupported | &cross; |
| [spatial](https://www.w3.org/TR/odrl-vocab/#term-spatial)                                   | unsupported | &cross; |
| [spatialCoordinates](https://www.w3.org/TR/odrl-vocab/#term-spatialCoordinates)             | unsupported | &cross; |
| [system](https://www.w3.org/TR/odrl-vocab/#term-system)                                     | unsupported | &cross; |
| [systemDevice](https://www.w3.org/TR/odrl-vocab/#term-systemDevice)                         | unsupported | &cross; |
| [timeInterval](https://www.w3.org/TR/odrl-vocab/#term-timeInterval)                         | unsupported | &cross; |
| [unitOfCount](https://www.w3.org/TR/odrl-vocab/#term-unitOfCount)                           | unsupported | &cross; |
| [version](https://www.w3.org/TR/odrl-vocab/#term-version)                                   | unsupported | &cross; |
| [virtualLocation](https://www.w3.org/TR/odrl-vocab/#term-virtualLocation)                   | unsupported | &cross; |


* The available implemented [Right Operands](https://www.w3.org/TR/odrl-vocab/#term-RightOperand) from those specified in the [ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/) are the following:

| Right Operands | Implementation status | # |
|--|--| -- |
| [policyUsage](https://www.w3.org/TR/odrl-vocab/#term-policyUsage) | unsupported  | &cross; |

### ODRL actions

* The available implemented [Right Operands](https://www.w3.org/TR/odrl-vocab/#term-RightOperand) from those specified in the [ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/) are the following:

| Actions                                                           | Implementation status | # |
|-------------------------------------------------------------------|--| -- |
| [policyUsage](https://www.w3.org/TR/odrl-vocab/#term-policyUsage) | unsupported  | &cross; |


### Extensions

In order to include new operators or operands a user must provide their name space and a function prefix for it. For instance, the new function <http://XXXXX> and its function prefix fnc_. Then, the user must implement the function fnc_XX in the file python functions
