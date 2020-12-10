import mysql.connector
from webpage_work import infobox_dict


class makeDB(object):

    def __init__(self, name, dict):
            #super(, self).__init__()
            self.name = name
            self.dict = dict


        def fname(arg):
def combine_CSV():
    list_of_CSVs = ['cpi.csv', 'disposable_income.csv','house_hold_debt.csv', 'house_hold_financial_assets.csv' ,
                          'house_hold_financial_transactions.csv', 'house_hold_networth.csv', 'house_hold_savings.csv', 'housing _prices.csv', 'hous_hold_spending.csv',
                          'interest.csv', 'price_level_indicies.csv', 'share_prices.csv']

    country_indicators_dict =[]
    country_indicator_list = []

    for i in list_of_indicators:
        filename = i
        with open(f'{file_path}\{file_name}') as csvfile:
            a = csv.reader(csvfile, delimiter=',')

            for row in a:
                items_dict = {'Location': row[0], 'Indicator':row[1], 'value': row[6], 'Year': row[5]}
                items_list = (row[0], row[1], row[6], row[5])
                country_indicators_dict.append(items_dict)
                country_indicator_list.append(items_list)

def prep_data():

    countries = []
    inidcators = []

    for i in country_indicator_list:
        counry_inicator_rows = i
        country_name = i[0]
        countries.append(country_name)
        inidcator_name = i[1]
        inidcators.append(inidcator_name)

def create_db():

    db = mysql.connector.connect(
        host = '',
        #3306',
        user = '',
        password = ''
    )

    cursorObject = db.cursor()
    mycursor = db.cursor()

    mycursor.execute(f"CREATE DATABASE {DBNAME}")

#def create_table():

#def populate_db():
create_db()
