from common.helpers import strip_whitespace, randomword
from common.data import text_extract
from datetime import datetime
import re


def import_file(file):
    text = text_extract(file)
    group = randomword(8)
    time_log = "{:%B %d, %Y}".format(datetime.now())
    string = text.decode('utf-8').replace("|", " ").replace("  ", "")
    html = {}
    no = re.findall(r"([0-9]+)\.", string)
    t = re.split(r"[0-9]+\.", string)
    title = t[0].split("\n")
    title = re.split(":", title[1])
    unit = {
        'title': title[1],
        'unit': title[0]
    }
    t.remove(t[0])
    quest = []
    for idx, val in enumerate(t):
        # va = val.replace("\n", "")
        html["no"] = no[idx]
        html["test_id"] = group
        html["logdate"] = time_log
        html["id"] = randomword(8)
        qu = re.split(r"[a-z]\)", val)
        opts = []
        for i, ix in enumerate(qu):
            if i == 0:
                html["LO"] = (re.findall(r'\(LO([0-9])\)', ix))[0]
                html["question"] = re.sub(r'(\(LO([0-9])\))', "", ix).replace('\n', ' ')
            else:
                opts.append({"option": ix.replace('\n', ' '), "score": ""})
        html["options"] = opts

        quest.append(html.copy())
    print("print quest :", quest)
    unit["questions"] = quest
    strip_whitespace(unit)
    return unit


def import_stream(file):
    group = randomword(8)
    time_log = "{:%B %d, %Y}".format(datetime.now())
    string = file.replace("|", " ").replace("  ", "").replace(u'\ufeff', '')
    html = {}

    no = re.findall(r"\n([0-9]+)\.", string)
    # if re.match(r"/[f,F]eedback:?.+?\n/", string):
    feedback = re.findall(r"([F,f]eedback:?.+?\n)", string)
    if feedback:
        string = re.sub(r"([F,f]eedback:?.+?\n)", "", string)
    string = re.sub(r"[*]", " ", string)
    t = re.split(r"\n[0-9]+\.", string)
    title = t[0].split("\n")
    title = re.split(":", title[0])
    unit = {
        'title': title[1],
        'unit': title[0]
    }
    t.remove(t[0])
    quest = []
    for idx, val in enumerate(t):
        html["no"] = no[idx]
        if len(feedback) > 0:
            html['Feedback'] = feedback[idx]
        # html["test_id"] = randomword(8)    # randomword used to identify question
        html["logdate"] = time_log

        question_id = randomword(8)
        html["question_id"] = question_id
        lo = re.findall(r'\([L,l]\w?([0-9]).?\d?\)', val)
        val = re.sub(r'\([L,l]\w?[0-9].?\d?\)', " ", val)
        qu = re.split(r"\n[a-d]\)", val)
        opts = []
        for i, ix in enumerate(qu):
            if len(lo) > 0:
                html["LO"] = lo[0]
            else:
                html['LO'] = ""
            if i == 0:
                html["question"] = ix.replace('\n', ' ')
            else:
                opts.append({"option": ix.replace('\n', ' '), "score": "", "option_id": question_id + "-" + str(i)})
        html["options"] = opts
        quest.append(html.copy())
    unit["questions"] = quest
    strip_whitespace(unit)
    return unit
