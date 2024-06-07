import pytest
import os
import zipfile
import shutil


os.getcwd()
FILES_DIR = os.path.join(os.getcwd(), 'files')
RESOURCES_DIR = os.path.join(os.getcwd(), "resources")

TEST_CSV = "file_example_XLSX_50.xlsx - Sheet1.csv"
TEST_XLSX = "file_example_XLSX_50.xlsx"
TEST_PDF = "Python Testing with Pytest (Brian Okken).pdf"


@pytest.fixture(scope="module", autouse=True)
def create_archive():
    if not os.path.exists("resources"):
        os.mkdir("resources")

    with zipfile.ZipFile(os.path.join(RESOURCES_DIR, "new_archive.zip"), 'w') as zf:
        for file in [TEST_CSV, TEST_XLSX, TEST_PDF]:
            add_file = os.path.join(FILES_DIR, file)
            zf.write(add_file, os.path.basename(add_file))

    yield
    shutil.rmtree(RESOURCES_DIR)
