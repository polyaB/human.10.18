import pandas as pd
import os
import xlrd

# file = open("data/1 СКЮ_2016.xlsx", 'r')
# f = file.readlines()
# data = pd.read_csv("data/1 СКЮ_2016.xlsx")
basedir = "data/"
for filename in os.listdir(basedir):
    print(filename)
    data = pd.read_excel(basedir + filename, skiprows=[0, 1, 2, 3])
    data_forVep = data[['Reference Accession Number', 'Start Position in Ref', 'End Position in Ref', ]]
    #print(df['Total Depth'])
# h = 'Reference Accession Number;Start Position in Ref;End Position in Ref;Reference Bases;Variation Bases;Total Variation Percent;Total Depth;Reference Amino Acids;Variation Amino Acids;Coding Frame;Region Name;Known SNP Info;Near SNP Info;Percent Forward With Variation;Percent Reverse With Variation;Num Forward With Variation;Num Reverse With Variation;Total Num Forward Reads;Total Num Reverse Reads;Targeted Region Status'
# print(list([i for i in h.split(';')]))
# #df = pd.read_csv("data/MID2_2014_столбцы_П_utf8.txt",sep=';', skiprows=[0,1,2,3])
# #it works only for .xlsx files
# df = pd.read_excel("data/7 ЛПА_2016.xlsx",skiprows=[0,1,2,3])#, comment='')#,usecols=list([i for i in h.split(';')]))
# # df1 = pd.read_csv("data/test.csv", sep=";", encoding= [
# # 'utf-8',
# # 'cp500',
# # 'utf-16',
# # 'GBK',
# # 'windows-1251',
# # 'ASCII',
# # 'US-ASCII',
# # 'Big5'
# # ])
# print(df['Total Depth'])
# print(df.keys())
# # print(df1)
# # print(data)
# # print(f)