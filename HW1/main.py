from HW1.application.salary import calculate_salary
from HW1.application.db.people import get_employees
import datetime

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.datetime.today())