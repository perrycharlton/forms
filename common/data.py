import textract, csv, json
from pathlib import Path


def text_extract(file):
    text = textract.process('static/data/' + file)
    return text


def text_extract1(file):
    text = textract.process(file)
    return text


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


def text_data1(file):
    print('got here')
    f = open("static/data/" + file, 'r')
    print(f)

    return f


def create_form():
    # get the page details then get the data from the form
    m_html = csv_data('user_form')

    return m_html


def json_file(file):
    f = open("static/data/" + file, "r")
    return json.load(f)


def quiz_json_file(file):
    f = open("quiz/quiz_static/data/" + file, "r")
    return json.load(f)


def quiz_json_to_file(file, file_name):
    file_path = "quiz/quiz_static/data/"
    if Path(file_path + file_name).is_file():
        with open("quiz/quiz_static/data/" + file_name, 'a') as outfile:
            json.dump(file, outfile, indent=2)
        return "ok"
