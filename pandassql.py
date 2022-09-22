from pandasql import sqldf
import pandas as pd
import os.path as op

def parse():
    import argparse

    parser = argparse.ArgumentParser(description='Make SQL command for couple of excels, for Samsung GA <3')
    parser.add_argument('--excels', type=str, nargs='+',
                        help='paths to excels')
    parser.add_argument('--sql', help='SQL command to play with exels')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args= parse()
    paths = [op.normpath(x) for x in args.excels]
    names = [op.splitext(op.basename(x))[0] for x in paths]
    query = args.sql

    dfs = {x[0]: pd.read_excel(x[1]) for x in zip(names, paths)}
    pysqldf = lambda q: sqldf(q, dfs)

    out = pysqldf(query)
    print(out.head())

    out.to_excel("output.xlsx")

