import pandas as pd


# pd.Series Одномекрным массивом данных
# pd.DataFrame Двумерный массив данных

def work_with_series():
    #        0         1      2       3
    data = ['Вася', 'Петя', 'Саша', 'Даша']
    # index = ['name1', 'name2', 'name3', 'name4']
    ds = pd.Series(data, index=['name1', 'name2', 'name3', 'name4'])

    # print(ds['name1'])

    print('=================\n\n')

    data2 = {
        'first_name': 'Владимир',
        'last_name': 'Петрович',
        'date_of_birth': '1990.03.10',
        'phone': '+7(961) 983-23-40',
    }

    ds_from_dict = pd.Series(data2)

    # ds_from_dict['married'] = True
    ds_from_dict_dropped = ds_from_dict.drop(labels=['phone', 'last_name'])
    ds_from_dict.drop('phone')  # inplace=True)

    print(ds_from_dict)
    print('============')
    print(ds_from_dict_dropped)
    #
    # print('=================\n\n')


def word_with_data_frame():
    # data = {
    #     'first_name': ['Владимир'],
    #     'last_name': ['Петрович'],
    #     'date_of_birth': ['1990.03.10'],
    #     'phone': ['+7(961) 983-23-40'],
    # }
    #
    # df = pd.DataFrame(data)
    #
    # print(df)
    # print('==================\n\n')

    data2 = [
        ['Вася', 12, '+7(961) 983-23-40'],
        ['Петя', 17, '+7(961) 983-23-80'],
        ['Дима', 13, '+7(961) 983-23-90'],
        ['Дима', 18, '+7(961) 983-23-90']
        #  0      1         2
    ]
    # columns = ['Имя', 'Возраст', 'Телефон']
    df2 = pd.DataFrame(data2, columns=['Имя', 'Возраст', 'Телефон'])

    df2['married'] = True

    print(df2)


# word_with_data_frame()


def work_with_xlsx():
    data__ = pd.read_excel('apartment_data.xlsx')
    print(data__)


# work_with_xlsx()
# # word_with_data_frame()
