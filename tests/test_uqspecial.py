import unittest
import jsonofabitch as jsob
import json

special = ["_", "-", "~", "$", "@", "&", "?", ".", "%", "<", ">", "#","!","^","+","/","*"]
datajsob = []
datacheck = []
for s in special:
    datajsob.append(
        f"b{s}ob:g=5, h{s}=4 ; {s}b=(6,6,3,), f=string{s}, l=[3,3,3,3,]",
    )
    datacheck.append(
        {f"b{s}ob": {"g": 5, f"h{s}": 4, f"{s}b": (6, 6, 3), "f": f"string{s}", "l": [3, 3, 3, 3]}}
    )


class TestJSOB(unittest.TestCase):
    def test_uqspecial(self):
        for j, d in enumerate(datajsob):
            self.assertEqual(jsob.loads(d), datacheck[j])


if __name__ == "__main__":
    unittest.main()
