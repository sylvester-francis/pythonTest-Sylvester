import os
import pytest
from xmlparser.xmlParser import read_file

def test_read_existing_file():
    filepath = 'existing_file.txt'
    with open(filepath, 'w'):
        result = read_file(filepath)
    assert result == filepath

def test_read_nonexistent_file():
    filepath = 'nonexistent_file.txt'
    with pytest.raises(FileNotFoundError, match=f"The specified file is not found: {filepath}"):
        read_file(filepath)

def test_read_file_exception():
    filepath = 'some_file.txt'
    with open(filepath, 'w'):
        with pytest.raises(Exception, match=f"An exception occured while trying to find the file: FileNotFoundError : Error message - "):
            read_file(filepath)

def test_read_file_returns_none():
    filepath = None
    result = read_file(filepath)
    assert result is None

def test_read_file_directory():
    directory_path = 'some_directory'
    os.makedirs(directory_path)
    with pytest.raises(FileNotFoundError, match=f"The specified file is not found: {directory_path}"):
        read_file(directory_path)
