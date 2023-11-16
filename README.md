## JSONofabitch

- fault tolerant json parser
- JSON correction/formatting engine
- stochastic ascii structured data format
- a standard for low standards
- the *retard proof* multi-parameter, multi-type input parser
- a troll of api scraping reverse engineers
- a JSON of a bitch!

functions
---------

- ``loads()`` - loads JSOB to dict
- ``dumps()`` - dumps regular json
- ``correct()`` - turns JSOB to JSON 
- ``sonofadumps()`` - dumps stochastic JSOB

JSOB syntax
-----------

- JSOB objects can be enclosed in ``{ }`` brackets, but its not required, they can be terminated with ';' 
- keypairs -  ``:`` or ``=`` separate key value pairs, whitespace is ignored  
- keys - quoted string or alphanumeric plus underscore, non-numeric first character(same as python vars). double quotes only
- values - another JSOB object, a tupple, a list, alphanumeric string without quotes, quote-enclosed string, boolean ``true`` ``false`` , ``null`` , numbers
- keypairs in a JSOB object are separated by ``;`` or ``,``, JSOB objects can be terminated by ``;;`` or ``;,`` when nested as values in keypairs or lists and unenclosed in brackets
- ``'true' -> True`` ``'false' -> False`` ``'null' -> None`` case sensitive
- tuples are enclosed in ``( )`` lists in ``[ ]``  comma punctuated trailing comma is okay.
- other - unquoted strings must be alphanumeric plus ``_``. only double quotes can be used
- scientific notation ``2e4`` resolves to $2.0 * 10^4$, always resolve to float
- numbers with decimal present resolve to floats while others resolve to ints IE ``'3.0' -> 3.0`` and ``'3' -> 3`` ``'3.' -> 3.0``


conventions
-----------

called JSOB(*jay-sawb*) or JSLOB in polite company

suggested file extension ``.sob`` or ``.jsob`` 
