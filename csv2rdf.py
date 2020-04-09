from cow_csvw.csvw_tool import COW
import os

#filename = 'cow_person_example.csv'
# path = 'C:\\Users\\Roger\\githome\\krst_covid19'
filename = 'COVID19_Fallzahlen_CH_total.csv'
path = '.'

# build a meta file
# COW(mode='build', files=[os.path.join(path, filename)], dataset='My dataset', delimiter=';', quotechar='\"', base='http://rogers.li/covid19/')

# convert the csv into rdf
COW(mode='convert', files=[os.path.join(path, filename)], dataset='My dataset', delimiter=';', quotechar='\"', processes=1, chunksize=100, base='http://rogers.li/covid19/')
