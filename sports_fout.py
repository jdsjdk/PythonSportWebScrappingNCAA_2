'''
Author: Jess Summerhill
Project: A sport betting analytics web scrapper
Date: 2-29-2020

This is where I set the framework for ouputting to a file.
I will be for this version, using CSV, and then file IO.
'''

import csv
from datetime import date as d
from pathlib import Path as fp


class SportsFileOut:
    def __init__(self):
        return None

    def save_file_format(self):
        # A simple funtion that saves the correct file format
        t = d.today()
        mm = str(t.month)
        dd = str(t.day)
        yy = str(t.year)
        ftm = "_" + mm + "_" + dd + "_" + yy
        fname = "ncaa_stats" + ftm + ".csv"

        return fname

    def output_csvfile(self, fname, fkey, keysl=[], dic_list=[]):
        # Get the file path, write the folder and the file name, output the CSV file
        fheaders = []
        p = fp("ouput/")
        p.mkdir(parents=True, exist_ok=True)
        fpath = p / fname

        with fpath.open("w", encoding="utf-8") as f:

            fheaders.append(fkey)

            for k in keysl:
                fheaders.append(k)

            fwriter = csv.DictWriter(
                f, dialect="excel", fieldnames=fheaders, delimiter='\t')

            fwriter.writeheader()

            for row in dic_list:
                fwriter.writerow(row)

        return None


sfout = SportsFileOut()
