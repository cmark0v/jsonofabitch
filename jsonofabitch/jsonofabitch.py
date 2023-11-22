import sys

__all__ = (
    "loads",
    "dumps",
    "correct",
    "dumpslob",
)

from .jsob import Lark_StandAlone, Transformer, v_args
from random import random


class TreeToJson(Transformer):
    @v_args(inline=True)
    def string(self, s):
        return (
            s.replace('"', '\\"')
            .rstrip('"')
            .strip("\\")
            .lstrip('"')
            .replace('\\\\"', '"')
        )

    @v_args(inline=True)
    def numb(self, s):
        if "." in s or "e" in s:
            return float(s)
        return int(s)

    def duct(self, s):
        try:
            return dict(s)
        except TypeError:
             return {}

    def tup(self,s):
        if tuple(s) == (None,):
            return ()
        else:
            return tuple(s)

    def lis(self,s):
        if list(s) == [None]:
            return []
        else:
            return list(s)


    tuple = tup
    array = lis
    pair = tuple
    object = duct
    number = v_args(inline=True)(numb)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


json_parser = Lark_StandAlone(transformer=TreeToJson())

parse = json_parser.parse


def loads(jsob_str: str) -> dict:
    """parses string of JSLOB compliant content"""
    return parse(jsob_str)


def dumps(data: dict, tuples=False) -> str:
    """writes out dictionary as string of compliant json, to dump tuples use tuples=True, otherwise they are converted to lists to comply with standard python ``json.loads()``"""

    def spew(numz):
        out = ""
        for j in numz:
            out = out + dumps(j, tuples=tuples) + ", "
        return out.rstrip(", ")

    if type(data) is str:
        return '"' + data.replace('"', '\\"') + '"'
    elif type(data) is float or type(data) is int:
        return str(data)
    elif data is None:
        return "null"
    elif data is True:
        return "true"
    elif data is False:
        return "false"
    elif type(data) is list:
        return "[" + spew(data) + "]"
    elif type(data) is tuple:
        if tuples:
            return "(" + spew(data) + ")"
        else:
            return "[" + spew(data) + "]"
    elif type(data) is dict:
        out = "{"
        for k in data.keys():
            kstr = str(k)
            out = out + f'"{kstr}": ' + dumps(data[k], tuples=tuples) + ", "
        out = out.rstrip(", ") + "}"
        return out


def correct(jsob_str: str) -> str:
    """reads JSLOB compliant syntax and outputs JSON compliant syntax"""
    return dumps(parse(jsob_str))


def randsp(mins=0, maxs=3):
    return mins * " " + int(random() * maxs) * " " + ""


def randl():
    if random() > 0.5:
        return "="
    else:
        return ":"


def randc(col=False):
    if random() > 0.5:
        return ","
    elif col:
        return ";"
    else:
        return " "


def randend():
    if random() > 0.5:
        return "}"
    else:
        return ";"


def randq(s, p=0.5):
    if random() > p or s[0].isdigit() or not s.replace("_", "").isalnum():
        return '"' + s.replace('"', '\\"') + '"'
    else:
        return s


def dumpslob(data) -> str:
    """Dump Stochastically Lacerated Objects. dumps stoachastically perterbed JSLOB compliant text from tuple, list, dict"""

    def spew(numz):
        out = ""
        for j in numz:
            out = out + randsp(0, 2) + dumpslob(j) + randsp(0, 2) + ","
        return out.rstrip(",") + randc()

    if type(data) is str:
        return randq(data)
    elif type(data) is float:
        return str(data).rstrip("0") + "0" * int(random() * 3)
    elif type(data) is int:
        return str(data)
    elif data is None:
        return "null"
    elif data is True:
        return "true"
    elif data is False:
        return "false"
    elif type(data) is list:
        return "[" + spew(data) + "]"
    elif type(data) is tuple:
        return "(" + spew(data) + ")"
    elif type(data) is dict:
        if random() > 0.5:
            out = ""
        else:
            out = "{"
        for k in data.keys():
            out = (
                out
                + randsp()
                + randq(k)
                + randl()
                + randsp()
                + str(dumpslob(data[k]))
                + randc(col=True)
            )
        out = out[0:-1] + randend()
        return out


__all__ = (
    "loads",
    "dumps",
    "correct",
    "dumpslob",
)
