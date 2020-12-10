from app import people as p
from datetime import datetime
import os


def parametrized_logger(file_path):
    call_qty = 0

    def logger(func):
        def new_func(*args, **kwargs):
            nonlocal call_qty
            call_qty += 1
            result = func(*args, **kwargs)
            now = datetime.today().strftime("%d.%m.%Y %H:%M:%S")
            if os.path.exists(file_path):
                f_mode = 'a'
            else:
                f_mode = 'w'
            with open(file_path, f_mode) as file:
                file.write(
                    f'{call_qty} | Дата и время:{now} | Имя: {func.__name__} | Аргументы: {args, kwargs} | '
                    f'Возвращаемое значение: {result} \n'
                )
            return result

        return new_func

    return logger


@parametrized_logger('logs.txt')
def calculate_salary(employees, months):
    return sum([e['salary'] * months for e in employees])


if __name__ == '__main__':
    calculate_salary(p.get_employees(), 3)
    calculate_salary(p.get_employees(), 2)
    calculate_salary(p.get_employees(), 10)
