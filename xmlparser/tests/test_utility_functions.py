from argparse import Namespace
import pytest
from unittest.mock import patch
from parser.utility_functions import return_args

def test_return_args():
    with patch('argparse.ArgumentParser.parse_args', return_value=Namespace(filepath='/path/to/xml/file.xml')):
        args = return_args()
        assert args.filepath == '/path/to/xml/file.xml'