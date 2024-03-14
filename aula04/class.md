## Diagram

``` mermaid

classDiagram

class Character {
    +name: str
    +race: str
    +class: str
    +level: int
    +skill_collection: array
    +Character(name: str, race: str, class: str, level: int)
    +addSkill(skill: Skill): void
    +useSkill(skillName: str): void
    +levelUp(): void
}

class Skill {
    +skill_name: str
    +skill_elemental: str
    +skill_level: int
    +skill_damage: int
    +Skill(skill_name: str, skill_elemental: str, skill_level: int, skill_damage: int)
}

class Inventory {
    +items: array
    +Inventory()
    +addItem(item: Item): void
    +removeItem(item: Item): void
}

class Item {
    +name: str
    +type: str
    +effect: str
    +Item(name: str, type: str, effect: str)
}

Character "1" --> "0..*" Skill : has



```