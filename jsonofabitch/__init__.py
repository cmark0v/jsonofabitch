"""

functions
---------

- ``loads()`` - loads JSLOB compliant text 
- ``dumps()`` - dumps regular JSON
- ``correct()`` - turns JSLOB to JSON 
- ``dumpslob()`` - dumps stochastic JSLOB


JSLOB syntax
------------

- keypairs -  ``:`` or ``=`` separate key value pairs, whitespace is ignored  ``'g=5' -> {"g": 5}`` and ``'g:5' -> {"g": 5}``, such keypairs are implicitly assumed to be in a JSLOB object which resolves to a python dict
- keys - double quoted string or alphanumeric plus underscore, non-numeric first character(same as python vars). 
- values - another JSLOB object, a tupple, a list, alphanumeric string without quotes, quote-enclosed string, boolean ``true`` ``false`` , ``null`` , integers, floats
- ``'true' -> True`` ``'false' -> False`` ``'null' -> None`` case sensitive
- tuples in ``( )`` lists in ``[ ]`` objects separated by comma ``,`` or semicolon ``;`` . trailing comma/semicolon okay
- dicts/JSLOB objects have keypairs separated by semicolon or comma, nested jslob objects(in lists, tuples or jslob objects) are terminated and separated simultaneously by ``;;`` or ``,,`` , IE: ``'[g=5,h=3]' -> [{'g': 5, 'h': 3}]`` and ``'[g=5;;h=3]' -> [{'g': 5}, {'h': 3}]``
- other - unquoted strings must be alphanumeric plus ``_`` non-numeric first character. only double quotes can be used
- scientific notation ``2e4`` resolves to $2.0 * 10^4$, always resolve to float
- numbers with decimal present resolve to floats while others resolve to ints IE ``'3.0' -> 3.0`` and ``'3' -> 3`` ``'3.' -> 3.0``


examples
--------

```python
import jsonofabitch as jsob
d = jsob.loads("f=5, size=big, style=SLOB, coord=[(3,4),(1.2,3)]")
#{'f': 5, 'size': 'big', 'style': 'SLOB', 'coord': [(3, 4), (1.2, 3)]}

jsob.dumps(d)
#Out[3]: '{"f": 5, "size": "big", "style": "SLOB", "coord": [[3, 4], [1.2, 3]]}'

jsob.dumpslob(d)
#Out[4]: ' "f"=  5;  "size"="big";style=  "SLOB";  coord: [ (3 ,4 ), (1.2, 3,)  ];'

jsob.dumpslob(d)
#Out[5]: ' "f"= 5;size="big", style: SLOB, "coord": [ (3, 4 ),(1.2 , 3  ) ];'

jsob.dumpslob(d)
#Out[6]: ' "f"= 5,  size=  "big",style=  "SLOB";  coord:  [ (3,4 ,) ,(1.2 , 3,)  ];'
```
"""

__version__: str = "0.3.2"


from .jsonofabitch import __all__
from .jsonofabitch import *
