import re
def check_phone(phone):
    if (phone[0] == '7') or (len(phone) == 10):
        return True
    else:
        return False

def check_city(city):
    return city.lower() == "москва"

def check_application(city, phone):
    return check_city(city) and check_phone(phone)


def find_valid_applications(applications):
    for app in applications:
        print(app, "---", bool(re.match(r"name=.*,phone=[78][0-9]{9},city=москва", app.lower().replace(" ", ""))))




applications = [
        'name=Аня,phone=8800234 ,city=москва',
        'name=КОЛЯ,phone=8800900871 ,city=МОСКВА',
        'name=Валентина,phone=7950900871 ,city=волгоград',
        'name=,phone=7999901871,city=москва',
        'name=Иван,phone=7999901871,city=москва',
        'name=Инга,phone=,city=москва']
print(find_valid_applications(applications))