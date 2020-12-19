import csv
from oecd_data import *
import mysql.connector
import pandas as pd


def combine_CSV():
    list_of_csv = []

    csv_dict =[]
    csv_list = []

    for i in list_of_csv:
        filename = i
        with open(f'oecd_data\{filename}') as csvfile:
            a = csv.reader(csvfile, delimiter=',')

            for row in a:
                items_dict = {'Location': row[0], 'Indicator':row[1], 'value': row[6], 'Year': row[5]}
                items_list = (row[0], row[1], row[6], row[5])
                country_indicators_dict.append(items_dict)
                country_indicator_list.append(items_list)
    return country_indicators_dict
a = combine_CSV()
print
df = pd.DataFrame(a)
print(df)



def prep_data():

    countries = []
    indicators = []

    for i in country_indicator_list:
        counry_inicator_rows = i
        country_name = i[0]
        countries.append(country_name)
        inidcator_name = i[1]
        indicators.append(inidcator_name)
    countries = set(countries)
    indicators = set(indicators)
    return countries, indicators


prepped_data = prep_data()
countries = prepped_data[0]
indicators = prepped_data[1]
print(countries)









#'cpi.csv', 'disposable_income.csv','house_hold_debt.csv', 'house_hold_financial_assets.csv' , 'house_hold_financial_transactions.csv', 'house_hold_networth.csv', 'house_hold_savings.csv', 'housing _prices.csv', 'hous_hold_spending.csv', 'interest.csv', 'price_level_indicies.csv', 'share_prices.csv'
