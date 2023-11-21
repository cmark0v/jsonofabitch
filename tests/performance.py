import jsonofabitch as jsob
import json
from time import process_time


def main():
    datajsob = [
        '"bob":g=5, h=4 ; b=(6,6,3,), f=4, l=[3,3,3,3,]',
        '"bob":g=5, h=4 ;; b=(6,6,3,), f=4, l=[3.0,3.0,3.0,3,]',
        '"bob":g=5, h=4 ;, b=(6,6,3,), f=4, l=[3,"3",e3,3,]',
    ]


    datacheck = [
        {"bob": {"g": 5, "h": 4, "b": (6, 6, 3), "f": 4, "l": [3, 3, 3, 3]}},
        {"bob": {"g": 5, "h": 4}, "b": (6, 6, 3), "f": 4, "l": [3.0, 3.0, 3.0, 3]},
        {"bob": {"g": 5, "h": 4}, "b": (6, 6, 3), "f": 4, "l": [3, "3", "e3", 3]},
    ]
    dataslob = []
    data = []
    datadict={}
    for j in range(5000):
        datacheck[j% len(datacheck)]["bob"]["g"]=j
        dataslob.append(jsob.dumpslob(datacheck[j % len(datacheck)]))
        data.append(jsob.dumps(datacheck[j % len(datacheck)]))
        datadict[f"a{j}"] = (j%1000)*"fsf"
    bigdict = jsob.dumps(datadict)
    t1 = process_time()
    for d in data:
        json.loads(d)
    t2 = process_time()
    print(t2 - t1, "json python native")

    t1 = process_time()
    for d in data:
        jsob.loads(d)
    t2 = process_time()
    print(t2 - t1, " jsob json data")

    t1 = process_time()
    for d in dataslob:
        jsob.loads(d)
    t2 = process_time()
    print(t2 - t1, "jsob jslob data")

    t1 = process_time()
    f = jsob.loads(bigdict)
    t2 = process_time()
    print(t2 - t1, "jsob big dictdt")

    t1 = process_time()
    f = json.loads(bigdict)
    t2 = process_time()
    print(t2 - t1, "json big dictdt")

if __name__ == "__main__":
    main()
