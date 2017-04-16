
import csv
import json


def csv_data(file):
    print('got here: ' + file)
    try:
        f = open('static/data/' + file + '.csv', 'r')
    except IOError:
        f = open('static/data/user_form.csv', 'r')
    reader = csv.reader(f)
    my_list = list(reader)
    print(my_list)

    return my_list


def text_data(file):
    print('got here')
    f = open("static/data/" + file + '.txt', 'r')
    print(f)

    return f

def create_form():
    # get the page details then get the data from the form
    m_html = csv_data('user_form')

    return m_html


def json_file(file):
    f = open("static/data/" + file, "r")
    return json.load(f)
