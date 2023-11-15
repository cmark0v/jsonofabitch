import sys

from lark import Lark, Transformer, v_args
from random import random

json_grammar = r"""
    ?start: value

    ?value: object
          | array
          | tuple
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    array  : "[" [value ("," value )*] [","]"]"
    tuple  : "(" [value ("," value )*] [","]")"
    object : ["{"] pair [ ((","|";" ) pair )*] [","] ["}"|";"]
    pair   : string (":" | "=") value 
    
    string : CNAME|ESCAPED_STRING 

    %import common.CNAME
    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS

    %ignore WS
"""


class TreeToJson(Transformer):
    @v_args(inline=True)
    def string(self, s):
        return s.strip('"').replace('\\"', '"')

    @v_args(inline=True)
    def numb(self, s):
        if "." in s:
            return float(s)
        return int(s)

    tuple = tuple
    array = list
    pair = tuple
    object = dict
    number = v_args(inline=True)(numb)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


json_parser = Lark(
    json_grammar,
    parser="lalr",
    lexer="basic",
    propagate_positions=False,
    maybe_placeholders=False,
    transformer=TreeToJson(),
)
parse = json_parser.parse


def loads(jsob_str: str) -> dict:
    """parses string of JSOB compliant content to a dict, numbers become floats, lists resolve to lists, nested JSOB becomes dicts, tuples resolve"""
    if ("=" in jsob_str) + (":" in jsob_str):
        return parse(jsob_str)
    return {}


def dumps(data: dict) -> str:
    """writes out dictionary as string of compliant json"""

    def spew(numz):
        out = ""
        for j in numz:
            out = out + dumps(j) + ", "
        return out.rstrip(", ")

    if type(data) is str:
        return f'"{data}"'
    elif type(data) is float or type(data) is int:
        return str(data)
    elif type(data) is list:
        return "[" + spew(data) + "]"
    elif type(data) is tuple:
        return "(" + spew(data) + ")"
    elif type(data) is dict:
        out = "{"
        for k in data.keys():
            out = out + f'"{k}":' + dumps(data[k]) + ", "
        out = out.rstrip(", ") + "}"
        return out


def correct(jsob_str: str) -> str:
    """reads JSOB compliant syntax and outputs JSON compliant syntax"""
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
    if random() > p or not s.isalnum():
        return '"' + s + '"'
    else:
        return s


def sonofadumps(data) -> str:
    def spew(numz):
        out = ""
        for j in numz:
            out = out + randsp(0, 2) + sonofadumps(j) + randsp(0, 2) + ","
        return out.rstrip(",") + randc()

    if type(data) is str:
        if data.isalnum():
            return data
        else:
            return '"' + data + '"'
    elif type(data) is float:
        if random() > 0.3:
            return str(data) + "0" * int(random() * 2)
        else:
            return str(data)
    elif type(data) is int:
        return str(data)
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
                + str(sonofadumps(data[k]))
                + randc(col=True)
            )
        out = out[0:-1] + randend()
        return out


__all__ = (
    "loads",
    "dumps",
    "correct",
    "sonofadumps",
)
