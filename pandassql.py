from pandasql import sqldf
import pandas as pd
import os.path as op

def parse():
    import argparse

    parser = argparse.ArgumentParser(description='Make SQL command for couple of excels.')
    parser.add_argument('--sql', help='SQL command to play with exels', required=True)
    parser.add_argument('--excels', type=str, nargs='+', help='paths to excels')
    parser.add_argument('--csv', type=str, nargs='+', help='paths to csv')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args= parse()

    excel_dfs = {}
    csv_dfs = {}

    if args.excels is not None:
        excel_paths = [op.normpath(x) for x in args.excels]
        excel_names = [op.splitext(op.basename(x))[0] for x in excel_paths]
        excel_dfs = {x[0]: pd.read_excel(x[1]) for x in zip(excel_names, excel_paths)}

    
    if args.csv is not None:
        csv_paths = [op.normpath(x) for x in args.csv]
        csv_names = [op.splitext(op.basename(x))[0] for x in csv_paths]
        csv_dfs = {x[0]: pd.DataFrame(pd.read_csv(x[1])) for x in zip(csv_names, csv_paths)}

    
    query = args.sql

    dfs = {**excel_dfs, **csv_dfs}
    pysqldf = lambda q: sqldf(q, dfs)

    out = pysqldf(query)
    print(out.head())

    out.to_excel("output.xlsx")

