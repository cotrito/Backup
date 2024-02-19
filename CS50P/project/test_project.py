from proyect import table_exist, show_menu, chose_table
import pytest
import mock

def test_table_exist():
    assert table_exist('table1') == True

def test_chose_table(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    module_mocked = 'test_proyect'
    mock_target = f"{module_mocked}.table_exist"
    with mock.patch(mock_target, return_value=True):
        assert chose_table() == '1'

def test_show_menu():
    assert show_menu() == [{'Id': 'id', 'Item': 'item', 'Price': 'price'}, {'Id': '1', 'Item': 'cheese burguer', 'Price': '8'}, {'Id': '2', 'Item': 'clasic burguer', 'Price': '8'}, {'Id': '3', 'Item': 'pizza small', 'Price': '8'}, {'Id': '4', 'Item': 'pizza medium', 'Price': '10'}, {'Id': '5', 'Item': 'pizza large', 'Price': '12'}, {'Id': '6', 'Item': 'nachos', 'Price': '4'}, {'Id': '7', 'Item': 'cheese nachos', 'Price': '6'}, {'Id': '8', 'Item': 'french fries small', 'Price': ' 3'}, {'Id': '9', 'Item': 'french fries large', 'Price': ' 5'}, {'Id': '10', 'Item': 'coke', 'Price': '2.5'}, {'Id': '11', 'Item': 'water', 'Price': '1.5'}, {'Id': '12', 'Item': 'beer', 'Price': '4'}, {'Id': '20', 'Item': 'juice', 'Price': '3'}]