from sqlalchemy import event
from .user import User
from .asset import Asset
from .asset_category import AssetCategory
from .attribute import Attribute
from .push_id import PushID


def fancy_id_generator(mapper, connection, target):
    """A function to generate unique identifiers on insert."""
    push_id = PushID()
    target.id = push_id.next_id()


# associate the listener function with models, to execute during the
# "before_insert" event
tables = [
    Asset,
    AssetCategory,
    Attribute
]

for table in tables:
    event.listen(table, 'before_insert', fancy_id_generator)
