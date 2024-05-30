from src.item.data.aspect import Aspect
from src.item.data.item_type import ItemType
from src.item.data.rarity import ItemRarity
from src.item.models import Item


class TestLegendary(Item):
    def __init__(self, codex_upgrade=False, **kwargs):
        super().__init__(rarity=ItemRarity.Legendary, item_type=ItemType.Shield, power=910, codex_upgrade=codex_upgrade, **kwargs)


aspects = [
    ("upgrade", ["all", "upgrade"], TestLegendary(aspect=Aspect(name="of_anemia", value=30), codex_upgrade=True)),
    ("no upgrade", ["all"], TestLegendary(aspect=Aspect(name="of_anemia", value=30))),
]
