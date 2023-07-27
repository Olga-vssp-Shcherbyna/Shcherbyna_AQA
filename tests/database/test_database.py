import pytest
import sqlite3
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)
    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    bisquits_qnt = db.select_product_qnt_by_id(4)
    assert bisquits_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "тестові", "дані", 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)
    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


@pytest.mark.database
def test_quantity_type():
    db = Database()
    db.insert_product(99, "тестові", "дані", 999)
    assert type(db.select_product_qnt_by_id(99)[0][0]) == int
    db.delete_product_by_id(99)


@pytest.mark.database
def test_added_product_name():
    db = Database()
    db.insert_product(7, "холодець", "з хріном", 1)
    jelly = db.select_product_name_by_id(7)
    assert jelly[0][0] == "холодець"
    db.delete_product_by_id(7)


@pytest.mark.database
def test_add_invalid_product_description_type():
    db = Database()
    with pytest.raises(sqlite3.OperationalError):
        db.insert_product(7, "холодець з добавками", ["сало", "ковбаса"], 1)
    assert len(db.select_product_name_by_id(7)) == 0


@pytest.mark.database
def test_add_product_with_invalid_id_type():
    db = Database()
    pre_qnt = db.select_product_qnt_by_id(db.select_product_length())
    with pytest.raises(sqlite3.OperationalError):
        db.insert_product(
            {"key0": "val0", "key1": "val1"}, "холодець з добавками", "сало", 136
        )
    after_qnt = db.select_product_qnt_by_id(db.select_product_length())
    assert pre_qnt == after_qnt


@pytest.mark.database
def test_double_product_quantity():
    db = Database()
    db.insert_product(70, "печиво", "солоне", 30)
    bisquits_qnt = db.select_product_qnt_by_id(70)[0][0]
    db.insert_product(70, "печиво", "солоне", bisquits_qnt * 2)
    bisquits_new_qnt = db.select_product_qnt_by_id(70)[0][0]
    assert bisquits_new_qnt == bisquits_qnt * 2
