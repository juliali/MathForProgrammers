from chinese_calendar import is_workday, is_holiday
from datetime import date
import datetime

total_price = 120


def calculate_ticket_prince(the_day, gender, age, is_student, is_with_children):

    children_day = datetime.date(the_day.year, 6, 1)
    women_day = datetime.date(the_day.year, 3, 8)

    if the_day == women_day and gender == "F":
        return 0, "祝女性朋友节日快乐"

    if the_day == children_day and age <= 12:
        return 0, "祝小朋友们节日快乐"

    if age < 6:
        return 0, "祝小朋友游园快乐"

    if 6 <= age <= 12:
        return total_price / 3, "祝小朋友游园快乐"

    if 13 <= age <= 17:
        return total_price / 2, "祝同学们有缘快乐"

    if 18 <= age <= 22 and is_student:
        return total_price / 2, "请出示学生证"

    if 60 <= age <= 65:
        return total_price / 2, "请出示身份证"

    if age >= 66:
        return 0, "请出示身份证"

    if is_holiday(the_day):
        return total_price * 0.9, "节日快乐"
    elif the_day.weekday() == 0:
        return total_price * 0.8, "周一快乐"
    elif age >= 18 and is_with_children :
        return total_price * 0.9, "请照顾好同行的小朋友"

    return total_price, "祝您游园愉快"


def ticket_box_office_promot(the_day, gender, age, is_student, is_with_children):
    price, words = calculate_ticket_prince(the_day, gender, age, is_student, is_with_children)
    print("今天是 {0}，{1}，您的票价是 {2} 元".format(the_day, words, price))


ticket_box_office_promot(datetime.date(date.today().year, 6, 1), 'M', 11, True, False)
ticket_box_office_promot(datetime.date(date.today().year, 3, 8), 'F', 14, True, False)
ticket_box_office_promot(datetime.date(date.today().year, 4, 30), 'F', 18, True, False)
ticket_box_office_promot(datetime.date(date.today().year, 5, 1), 'F', 18, True, False)

ticket_box_office_promot(datetime.date(date.today().year, 5, 1), 'M', 25, False, False)
ticket_box_office_promot(datetime.date(date.today().year, 3, 8), 'F', 26, False, True)
ticket_box_office_promot(datetime.date(date.today().year, 6, 8), 'M', 37, False, True)
ticket_box_office_promot(datetime.date(date.today().year, 6, 10), 'M', 67, False, True)










