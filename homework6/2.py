import argparse

parser = argparse.ArgumentParser(description='Проверка даты.')
parser.add_argument('date', type=str, help='Дата для проверки в формате YYYY-MM-DD')

args = parser.parse_args()
date_to_check = args.date

if check_date(date_to_check):
    print(f"Дата {date_to_check} корректна.")
else:
    print(f"Дата {date_to_check} некорректна.")