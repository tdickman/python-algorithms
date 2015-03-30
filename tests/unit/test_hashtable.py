import pytest

import hashtable


@pytest.mark.unit
def test_add_item():
    ht = hashtable.HashTable()
    ht['test'] = 50
    assert ht['test'] == 50


@pytest.mark.unit
def test_add_items_collision():
    # Make everything colide
    hashtable.TABLE_SIZE = 1
    ht = hashtable.HashTable()
    ht['test1'] = 50
    ht['test2'] = 51
    assert ht['test1'] == 50
    assert ht['test2'] == 51


@pytest.mark.unit
def test_del_item():
    ht = hashtable.HashTable()
    ht['test'] = 100
    del ht['test']
    with pytest.raises(hashtable.errors.InvalidKey):
        ht['test']


@pytest.mark.unit
def test_del_invalid_item():
    ht = hashtable.HashTable()
    with pytest.raises(hashtable.errors.InvalidKey):
        del ht['test']


@pytest.mark.unit
def test_get_invalid_item():
    ht = hashtable.HashTable()
    with pytest.raises(hashtable.errors.InvalidKey):
        ht['test']
