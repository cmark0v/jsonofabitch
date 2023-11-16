import unittest
import jsonofabitch as jsob
import json

datajsob = [
    '"bob":g=5, h=4 ; b=(6,6,3,), f=4, l=[3,3,3,3,]',
    '"bob":g=5, h=4 ;; b=(6,6,3,), f=4, l=[3.0,3.0,3.0,3,]',
    '"bob":g=5, h=4 ;, b=(6,6,3,), f=4, l=[3,"3",e3,3,]',
    '"bob":g=5, h=4 ;, b=(6,6,3,), f=4, l=[3,"3",e:3;;3,]',
]


datacheck = [
    {"bob": {"g": 5, "h": 4, "b": (6, 6, 3), "f": 4, "l": [3, 3, 3, 3]}},
    {"bob": {"g": 5, "h": 4}, "b": (6, 6, 3), "f": 4, "l": [3.0, 3.0, 3.0, 3]},
    {"bob": {"g": 5, "h": 4}, "b": (6, 6, 3), "f": 4, "l": [3, "3", "e3", 3]},
    {"bob": {"g": 5, "h": 4}, "b": (6, 6, 3), "f": 4, "l": [3, "3", {"e": 3}, 3]},
]


class TestJSOB(unittest.TestCase):
    def test_loads(self):
        for j, d in enumerate(datajsob):
            self.assertEqual(jsob.loads(d), datacheck[j])

    def test_num(self):
        data = [
            "d=3.0",
            "d=3",
            "d=3e3",
            "d=3.0e3",
            "d=e3",
            "d=(2,2)",
            "d=[3,4,5]",
            "d=g:3,h:3",
            "d=true",
            "d=false",
        ]
        dout = [float, int, float, float, str, tuple, list, dict, bool, bool]
        for j, d in enumerate(data):
            self.assertTrue(type(jsob.loads(d)["d"]) is dout[j])

    def test_empty_plus_lists(self):
        data = [
            "{}",
            "",
            "sdfsdf",
            "5",
            "[5,5]",
            "[d=5,h=3]",
            "[d=5;,h=3]",
            "[d=5,,h=3,]",
            "[d=5;;h=3]",
            "(d=5;;h=3)",
            "(d=5;h=3;)",
            "{d=5;h=3;}",
            "{d=5,h=3,}",
            "d=5;h=3",
            "d=5,h=3,",
            "d=5,h=3;",
            "{d:d=5,h=3,}",
            "{d:d=5,,h=3,}",
            "d=d:5;;h=3",
        ]
        dout = [
            {},
            {},
            "sdfsdf",
            5,
            [5, 5],
            [{"d": 5, "h": 3}],
            [{"d": 5}, {"h": 3}],
            [{"d": 5}, {"h": 3}],
            [{"d": 5}, {"h": 3}],
            ({"d": 5}, {"h": 3}),
            ({"d": 5, "h": 3},),
            {"d": 5, "h": 3},
            {"d": 5, "h": 3},
            {"d": 5, "h": 3},
            {"d": 5, "h": 3},
            {"d": 5, "h": 3},
            {"d": {"d": 5, "h": 3}},
            {"d": {"d": 5}, "h": 3},
            {"d": {"d": 5}, "h": 3},
        ]
        for j, d in enumerate(data):
            self.assertEqual(jsob.loads(d), dout[j])

    def test_special(self):
        data = [
            "d=3.0e3",
            "d=true",
            "d=false",
            "d=null",
        ]
        dout = [3000.0, True, False, None]
        for j, d in enumerate(data):
            self.assertEqual(jsob.loads(d)["d"], dout[j])

    def test_dumps_compliance(self):
        for d in datajsob:
            di = jsob.loads(d)
            self.assertEqual(json.loads(json.dumps(di)), jsob.loads(json.dumps(di)))
            self.assertEqual(json.loads(jsob.dumps(di)), json.loads(json.dumps(di)))

    def test_dumps_tuples_self_compliant(self):
        for d in datajsob:
            di = jsob.loads(d)
            self.assertEqual(jsob.loads(jsob.dumps(di, tuples=True)), di)

    def test_dumpslob(self):
        for j in range(500):
            for d in datajsob:
                di = jsob.loads(d)
                du = jsob.dumpslob(di)
                try:
                    self.assertEqual(jsob.loads(du), di)
                except Exception as e:
                    print("SONOFADUMPS FAILING STRING: ", du)
                    raise (e)


#    def test_upper(self):
#        self.assertEqual('foo'.upper(), 'FOO')
#
#    def test_isupper(self):
#        self.assertTrue('FOO'.isupper())
#        self.assertFalse('Foo'.isupper())
#
#    def test_split(self):
#        s = 'hello world'
#        self.assertEqual(s.split(), ['hello', 'world'])
#        # check that s.split fails when the separator is not a string
#        with self.assertRaises(TypeError):
#            s.split(2)

if __name__ == "__main__":
    unittest.main()
