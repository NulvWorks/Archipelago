from typing import List

medals: List[str] = ["Copper", "Bronze", "Silver", "Gold", "Radiant"]

class Monster:
    """
    Data class for monsters
    """
    name: str
    minLevel: int
    maxLevel: int

    def __init__(self, name, min, max):
        self.name = name
        self.minLevel = min
        self.maxLevel = max

    def ultra(self) -> int:
        return 42 if self.maxLevel >= 8 else self.maxLevel*2

    def levelRange(self) -> range:
        return range(self.minLevel,self.maxLevel+1)

    def allLevelLocations(self, medal) -> List[str]:
        """Creates all locations in the form 'QP: Lv <level> <monsterName> <medalType> medal'"""
        res: List[str] = []
        for l in self.levelRange():
            res.append(f"QP – Lv {l} {self.name} – {medal} medal")
        return res

    def singleLevelLocation(self, medal) -> str:
        return f"QP – {self.name} – {medal} medal"
    
    def allUltraLocations(self, num) -> List[str]:
        return [f"UQP – Lv {l} {self.name} – {num} radiant medal{('s' if num>1 else '')}" for l in range(self.maxLevel+1, self.ultra()+1)]
        
    def singleUltraLocation(self, num) -> str:
        return f"UQP – {self.name} – {num} radiant medal{('s' if num>1 else '')}"

monsterList: List[Monster] = [
    # Shambles
    Monster("Scrambla",1,4),
    Monster("Shy Scrambla",5,8),
    Monster("Boiler",3,6),
    Monster("Rage Boiler",6,10),
    Monster("Knot Knott",1,6),
    Monster("Shiny Knot Knott",0,0),
    Monster("Blot",4,10),
    Monster("Avoidant Blot",7,11),
    Monster("Null Blot",6,12),
    Monster("Amalga",6,11),
    Monster("Calorie",3,9),
    Monster("Joule",7,12),
    Monster("Shiny Joule",0,0),
    Monster("Emerald",3,9),
    Monster("Moss",5,10),
    Monster("Shamra",4,12),
    # Guardians
    Monster("Rendy",1,4),
    Monster("Shiny Rendy",0,0),
    Monster("Snowball",7,10),
    Monster("Shiny Snowball",0,0),
    Monster("Roundsaw",1,6),
    Monster("Alter Roundsaw",5,7),
    Monster("Null Roundsaw",5,10),
    Monster("Lila",1,8),
    Monster("Shy Lila",3,11),
    Monster("Sandrome",4,11),
    Monster("Voladrome",6,12),
    Monster("Shanx",5,11),
    Monster("Alter Shanx",7,12),
    Monster("Ruby",3,9),
    Monster("Scarlet",5,10),
    Monster("Guardian Soul",4,12),
    # Eyeric Glyphs
    Monster("Photoxai",1,5),
    Monster("Dendrohai",1,7),
    Monster("Hematoren",2,7),
    Monster("Ombroah",1,8),
    Monster("Lavalin",5,9),
    Monster("Heliola",5,10),
    Monster("Chemory",3,11),
    Monster("Hadesoh",4,11),
    Monster("Chinotoh",5,11),
    Monster("Astrayo",5,12),
    Monster("Mononvai",7,12),
    Monster("Philolu",0,0),
    Monster("Topaz",3,9),
    Monster("Dandy",5,10),
    Monster("Oudenai",4,12),
    # Zaramechs
    Monster("Unit Lulu",1,3),
    Monster("Null Unit",4,11),
    Monster("Prisma",1,5),
    Monster("Rage Prisma",3,9),
    Monster("Dual Prisma",5,11),
    Monster("Syncron",2,9),
    Monster("Alter Syncron",7,10),
    Monster("Shiny Syncron",0,0),
    Monster("Flip Flap",4,9),
    Monster("Sentinel 4X",3,10),
    Monster("Sentinel 0X",5,11),
    Monster("Ventra",4,12),
    Monster("Sapphire",3,9),
    Monster("Indigo",5,10),
    Monster("Default",4,12),
    # Glass Flora
    Monster("Dot",1,5),
    Monster("Galcia",1,9),
    Monster("Alter Glacia",6,9),
    Monster("Null Glacia",5,10),
    Monster("Vitrea",2,8),
    Monster("Avoidant Vitrea",7,10),
    Monster("Rage Duet",5,12),
    Monster("Pearl",2,9),
    Monster("Momo",3,10),
    Monster("Shy Momo",5,11),
    Monster("Shiny Momo",0,0),
    Monster("Kiwi",6,12),
    Monster("Citrine",3,9),
    Monster("Amber",5,10),
    Monster("Echo",4,12),
    # Veyerals
    Monster("Split Veyeral",1,4),
    Monster("Burning Veyeral",1,5),
    Monster("Voltage Veyeral",1,6),
    Monster("Venom Veyeral",3,7),
    Monster("Frozen Veyeral",6,10),
    Monster("Vibrant Veyeral",7,11),
    Monster("Veyeral Quartet",3,11),
    Monster("Veyeral Rain",2,11),
    Monster("Shiny Veyerals",0,0),
    Monster("Storm Veyeral",5,11),
    Monster("Molten Veyeral",6,12),
    Monster("Blizzard Veyeral",6,12),
    Monster("Amethyst",3,9),
    Monster("Violet",5,10),
    Monster("Forma",4,12),
    Monster("The Void",4,11),
    Monster("Totaria",6,13),
    Monster("Blue Veyeral",5,13),
    # Special Monsters
    Monster("Wisp",1,1),
    Monster("Anomaly",2,2),
    Monster("Shiny Anomaly",0,0),
    Monster("Stella",3,3),
    Monster("Celestia",4,4),
    Monster("Unity",5,5),
    Monster("Chroma",6,6),
    Monster("Duality",7,7),
    Monster("Trinity",8,8),
    Monster("Avoidant Stella",9,9),
    Monster("Rage Celestia",10,10),
    Monster("Equinox",11,11),
    Monster("Octavia",12,12),
    Monster("Nix Polyps",3,12),
    Monster("Ember Polyps",6,13),
    Monster("Volt Polyps",6,13),
    Monster("Tox Polyps",6,13),
    Monster("Nova",3,12),
    Monster("Limbo",6,12)
]

s = 3

ll = [[m.singleUltraLocation(s)] + m.allUltraLocations(s) for m in monsterList]
fullList = [a for b in ll for a in b]

with open("res.json","w",encoding="utf-8") as f:
    for i, x in enumerate(fullList):
        f.write(f"\"{x}\": [109{i:04}, [\"ult_quick\"]],\n")