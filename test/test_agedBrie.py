import sys

sys.path.append(".")
from src.ollivanders import *
from tests import *

def test_agedBrie():
    
    items = gettests('Aged Brie')
    print(items)
    # for item in items:
    #     AgedBrie(item).update_quality()
    #     print(item.__repr__())

test_agedBrie()

