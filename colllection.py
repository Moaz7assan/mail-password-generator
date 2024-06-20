from rich.table import Table
from passwd_generator import default_passwd
from mail_generator import default_mail
import pandas as pd

data = {
        'Mail': [],
        'Firstname': [],
        'Surname': [],
        'Password': []
    }


def collection_df(mail, firstname, surname, passwd, table):
    data.setdefault('Mail', data.get('Mail').append(mail))
    data.setdefault('Firstname', data.get('Firstname').append(firstname))
    data.setdefault('Surname', data.get('Surname').append(surname))
    data.setdefault('Password', data.get('Password').append(passwd))

    df = pd.DataFrame(data=data)
    df = df.drop_duplicates(subset=['Mail'], keep=False)

    return df, table


def co_table():
    collection_table = Table(title='Collection')
    collection_table.add_column('Mail', justify='center', style='magenta')
    collection_table.add_column('Name', justify='left', style='cyan')
    collection_table.add_column('Password', justify='center', style='red')
    return collection_table


def default_collection(quantity, domain='popular'):
    collection_table = co_table()
    for x in range(quantity):
        firstname, surname, mail = default_mail(domain)
        passwd = default_passwd()
        collection_table.add_row(mail, firstname + ' ' + surname, passwd)
        collection = collection_df(mail, firstname, surname, passwd, collection_table)
    return collection


def custom_collection(quantity, domain):
    collection_table = co_table()
    for x in range(quantity):
        firstname, surname, mail = default_mail(domain=domain)
        passwd = default_passwd()
        collection_table.add_row(mail, firstname + ' ' + surname, passwd)
        collection = collection_df(mail, firstname, surname, passwd, collection_table)
    return collection

