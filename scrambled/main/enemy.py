import arcade

ENEMY_SCALING = 1.5


class Enemy(arcade.Sprite):
    """
    Base enemy sprite.

    movement_type controls behaviour:
      "stationary" – stays in place
      "patrol"     – moves horizontally between left_boundary and right_boundary,
                     reversing direction when either edge is reached
    """

    def __init__(
        self,
        center_x: float,
        center_y: float,
        movement_type: str = "stationary",
        speed: float = 2.0,
        left_boundary: float = 0.0,
        right_boundary: float = 0.0,
    ):
        super().__init__(":images:ufo-1.png", scale=ENEMY_SCALING)
        self.center_x = center_x
        self.center_y = center_y
        self.movement_type = movement_type
        self.speed = speed
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary

        if movement_type == "patrol":
            self.change_x = speed

    def update(self):
        if self.movement_type == "patrol":
            self.center_x += self.change_x
            if self.center_x >= self.right_boundary:
                self.center_x = self.right_boundary
                self.change_x = -self.speed
            elif self.center_x <= self.left_boundary:
                self.center_x = self.left_boundary
                self.change_x = self.speed
