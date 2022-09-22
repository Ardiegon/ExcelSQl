from pandasql import sqldf
import pandas as pd
from sklearn import datasets

worksers_df = pd.read_excel('pracownicy.xlsx',)
testers_df = pd.read_excel('podeszli.xlsx')
print(worksers_df) 