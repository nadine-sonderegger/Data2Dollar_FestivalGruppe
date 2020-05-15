
import re
import csv
import pandas as pd

#file = open("AnzahlArtikel.csv", "w")
list = dict()


#dataframe = pd.read_excel('Sentiment_Analysis_MC.xlsx', sheet_name="CompanyPositive")
#print(dataframe)

excel = pd.read_excel('Sentiment_Analysis_MC.xlsx', sheet_name="CompanyPositive")
list_of_tweets = excel['Company'].tolist()
list_of_startdates = excel['date'].tolist()
list_of_enddates = excel['enddate'].tolist()

print(list_of_tweets)
print(list_of_startdates)
print(list_of_enddates)

for x,y,z in zip(list_of_tweets, list_of_startdates, list_of_enddates):
    print('trump '+x)



#list = dataframe.to_dict('records')
#print(list)

#excel = pd.read_excel('Sentiment_Analysis_MC.xlsx', sheet_name="CompanyPositive", index_col[0,3]).to_dict(orient='index')
#for key in excel:
#    excel[key] = excel[key].values()[0]
#list = excel['ID'].to_dict()

#print(excel)

#news_impact = {'mael':[5547],'raoul':[8974],'nadine':[6947]}

#news_impact = {'Name':['Mael', 'Raoul', 'Nadine'],
                #'Result':[5547, 8974, 6947]}

#df = pd.DataFrame(news_impact)
#print(df)

#excel_output = pd.DataFrame(news_impact)
#excel_output = excel_output.swapaxes("index", "columns")
#excel_output.to_csv('outfile.csv')
