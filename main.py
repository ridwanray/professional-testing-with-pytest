from pydantic import ValidationError

from email_sender.email import send_email
from email_sender.reader import read_csv

FILE_PATH = "/home/ray/Desktop/employees.csv"


def main(file_path: str):

    try:
        employees: list = read_csv(file_path)

        for employee in employees:
            send_email(employee)

    except ValidationError as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    main(FILE_PATH)
