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
- ``sonofadump()`` - dumps stochastic JSOB

JSOB syntax
-----------

- JSOB objects can be enclosed in ``{ }`` brackets, but its not required, keypairs in a JSOB object are separated by ``;`` or ``,``, JSOB objects can be terminated by ``;;`` or ``,,`` or ``;,`` when nested as values in keypairs
- keypairs -  ``:`` or ``=`` separate key value pairs, whitespace is ignored  
- keys - quoted string or alphanumeric plus underscore, non-numeric first character(same as python vars)
- values - another JSOB object, a tupple, a list, alphanumeric string without quotes, quote-enclosed string, boolean ``true`` ``false`` , ``null`` , numbers
- ``'true' -> True`` ``'false' -> False`` ``'null' -> None case sensitive
- tuples are enclosed in ``( )`` lists in ``[ ]`` trailing comma is okay. comma punctuated 
- other - JSOB object resolves to dict, numbers resolve to floats, unquoted strings must be alphanumeric. only double quotes can be used
- scientific notation ``2e4`` resolves to $2 \prod 10^4$



conventions
-----------

called JSOB(*jay-sawb*) or JSLOB in polite company

suggested file extension ``.sob`` or ``.jsob`` 
