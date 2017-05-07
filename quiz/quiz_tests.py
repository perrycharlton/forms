from common import database


tests = database.Userdb('tests')
fs = database.Testdb()


def save_tests(test):
    if tests.find_one({"unit": test['unit']}) > 0:
        tests.find_one_update(
            {"unit": test['unit']},
            {
                "questions": {'$each': test["questions"]}
            })
    else:
        tests.create_user(
            {
                "title": test["title"],
                "unit": test['unit'],
                "questions": test["questions"],
                "user": test['user']
            })


def get_tests(test):
    if tests.find_one(test) > 0:
        exam = tests.find_user(test)
        print(exam)
        return exam


def save_images(images):
    for img in images:
        if fs.exists({"image_no": img['image_no']}):
            file = fs.find_one({"image_no": images['image_no']})
            print(file)
            pass
        else:
            file_id = fs.put(images)



