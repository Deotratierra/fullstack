#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from re import sub as re_sub
from sys import argv
from json import loads, dumps
from ast import literal_eval
import statistics as st

def process_raw_stats(content):
    for i, bench in enumerate(content["benchs"]):
        processed_results = []
        for arg in bench["results"]:
            results = {}
            results["mean"] = st.mean(arg)
            results["median"] = st.median(arg)
            results["stdev"] = st.stdev(arg)
            results["max"] = max(arg)
            results["min"] = min(arg)
            results["sum"] = sum(arg)
            processed_results.append(results)
        content["benchs"][i]["results"] = processed_results
    return content


def create_stats():
    source_file=argv[1]
    dest_file=argv[2]

    with open("%s.json" % source_file, "r") as jsonf:
        content = jsonf.read()

    content = process_raw_stats(
    	literal_eval(re_sub(r'\n|\s{1,30}', "", content))
    )
    out_filename = source_file if dest_file == "" else dest_file
    with open("%s.json" % out_filename, "w") as jsonf:
        jsonf.write(dumps(content, indent=4))


    #content = loads(content)

if __name__ == "__main__":
    create_stats()