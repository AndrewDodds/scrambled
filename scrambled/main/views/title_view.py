import arcade
from arcade import shape_list
from scrambled.main.views.level1_view import Level1View

TILE_SPRITE_SCALING = 2.0
PLAYER_SCALING = 0.6

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 640
WINDOW_TITLE = "Scrambled"
SPRITE_PIXEL_SIZE = 32
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SPRITE_SCALING
CAMERA_PAN_SPEED = 0.15

# Physics
MOVEMENT_SPEED = 5
JUMP_SPEED = 23
GRAVITY = 1.1

class TitleView(arcade.View):
    """Main application class."""

    def __init__(self):
        """
        Initializer
        """
        super().__init__()

        # Tilemap Object
        self.tile_map = None

        # Sprite lists
        self.shapes = shape_list.ShapeElementList()

        # Set up the player
        self.score = 0
        self.player_sprite = None

        self.physics_engine = None
        self.end_of_map = 0
        self.game_over = False

        self.game_camera = None
        self.gui_camera = None
        self.camera_bounds = None

        self.fps_text = None
        self.game_over_text = None

        self.level = 1
        self.max_level = 2

    def setup(self):
        """Set up the game and initialize the variables."""

        # Sprite lists

        #self.game_camera = arcade.Camera2D()
        #self.gui_camera = arcade.Camera2D()

        self.fps_text = arcade.Text('FPS:', 10, 10, arcade.color.BLACK, 14)
        self.game_over_text = arcade.Text(
            'Scrambled',
            self.window.center_x,
            self.window.center_y,
            arcade.color.BLACK, 30,
            anchor_x='center',
            anchor_y='center'
        )

        # Starting position of the player
        self.load_level(self.level)

        self.game_over = False

    def load_level(self, level):
        # layer_options = {"Platforms": {"use_spatial_hash": True}}

        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(
            ":maps:title.json", scaling=TILE_SPRITE_SCALING
        )



        # Calculate the right edge of the my_map in pixels
        self.end_of_map = self.tile_map.width * GRID_PIXEL_SIZE

        # --- Other stuff
        # Set the background color
        if self.tile_map.background_color:
            self.window.background_color = self.tile_map.background_color

        # This is a large rectangle that fills the whole
        # background. The gradient goes between the two colors
        # top to bottom.
        color1 = (0, 0, 64)
        color2 = (64, 128, 192)
        points = (
            (0, 0),
            (WINDOW_WIDTH, 0),
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            (0, WINDOW_HEIGHT),
        )
        colors = (color1, color1, color2, color2)
        rect = shape_list.create_rectangle_filled_with_colors(points, colors)
        self.shapes.append(rect)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        self.clear()

        self.shapes.draw()

        #with self.game_camera.activate():
            # Draw all the sprites.
        self.tile_map.sprite_lists["Background"].draw()

        for x in range(0, 1000, 100):
            for y in range (0, 1000, 100):
                output = f"x:{x},y:{y}"
                arcade.draw_text(output, x, y, arcade.color.RED)

       # with self.gui_camera.activate():
            # Put the text on the screen.
            # Adjust the text position based on the view port so that we don't
            # scroll the text too.
        output = f"FPS: {1/self.window.delta_time:.0f}"
        arcade.draw_text(
            output, 10, 20, arcade.color.BLACK, 14
        )

        if self.game_over:
            self.game_over_text.position = self.window.center
            self.game_over_text.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.SPACE:
            game_view = Level1View()
            game_view.setup()
            self.window.show_view(game_view)


    def on_update(self, delta_time):
        """Movement and game logic"""
        pass

