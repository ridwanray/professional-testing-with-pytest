import pytest
import os
import csv
from tempfile import NamedTemporaryFile

@pytest.fixture
def make_valid_csv_file():
    with NamedTemporaryFile(suffix=".csv", delete=False,mode="w") as temp_file:
        writer = csv.writer(
            temp_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )

        writer.writerow(["name", "email", "title", "phone"])
        writer.writerow(["Ray", "hi@ridwanray.com", "Engineer", "01234567890"])
        writer.writerow(["Ridwan", "mail.ridwanray@gmail.com", "Eng", "01234567890"])
    yield temp_file.name
    os.remove(temp_file.name)

@pytest.fixture(scope="function")
def make_invalid_csv_file():
    with NamedTemporaryFile(suffix=".csv", delete=False,mode="w") as temp_file:
        writer = csv.writer(
            temp_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )

        writer.writerow(["name", "email", "title", "phone"])
        writer.writerow(["Ray", "hi@ridwanray", "Engineer", "01234567890"])

    yield temp_file.name
    os.remove(temp_file.name)