import arcade
from enemy import Enemy

_LEVEL_CONFIGS = {
    1: [
        {"center_x": 400,  "center_y": 96, "movement_type": "stationary"},
        {"center_x": 800,  "center_y": 96, "movement_type": "patrol",
         "speed": 2.0, "left_boundary": 700, "right_boundary": 950},
    ],
    2: [
        {"center_x": 300,  "center_y": 96, "movement_type": "patrol",
         "speed": 2.5, "left_boundary": 200, "right_boundary": 500},
        {"center_x": 900,  "center_y": 96, "movement_type": "stationary"},
    ],
    3: [
        {"center_x": 500,  "center_y": 96, "movement_type": "patrol",
         "speed": 3.0, "left_boundary": 350, "right_boundary": 700},
        {"center_x": 1100, "center_y": 96, "movement_type": "patrol",
         "speed": 3.0, "left_boundary": 1000, "right_boundary": 1300},
    ],
    4: [
        {"center_x": 300,  "center_y": 96, "movement_type": "patrol",
         "speed": 3.5, "left_boundary": 150, "right_boundary": 500},
        {"center_x": 700,  "center_y": 96, "movement_type": "stationary"},
        {"center_x": 1200, "center_y": 96, "movement_type": "patrol",
         "speed": 3.5, "left_boundary": 1100, "right_boundary": 1400},
    ],
    5: [
        {"center_x": 250,  "center_y": 96, "movement_type": "patrol",
         "speed": 4.0, "left_boundary": 100, "right_boundary": 450},
        {"center_x": 700,  "center_y": 96, "movement_type": "patrol",
         "speed": 4.0, "left_boundary": 550, "right_boundary": 900},
        {"center_x": 1150, "center_y": 96, "movement_type": "patrol",
         "speed": 4.0, "left_boundary": 1000, "right_boundary": 1400},
    ],
}


class EnemySpawner:
    """Builds the enemy SpriteList for a given level."""

    def create_enemies(self, level: int) -> arcade.SpriteList:
        enemy_list = arcade.SpriteList()
        for config in _LEVEL_CONFIGS.get(level, []):
            enemy_list.append(Enemy(**config))
        return enemy_list
