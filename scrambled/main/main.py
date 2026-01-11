"""
Load a Tiled map file with Levels

Start point for the scramble game..

Artwork from: https://kenney.nl
Tiled available from: https://www.mapeditor.org/

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_tiled_map_with_levels
"""
import arcade
import views.title_view

TILE_SPRITE_SCALING = 0.5
PLAYER_SCALING = 0.6

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Scrambled"
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SPRITE_SCALING
CAMERA_PAN_SPEED = 0.15

# Physics
MOVEMENT_SPEED = 5
JUMP_SPEED = 23
GRAVITY = 1.1



def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game = views.title_view.TitleView()
    game.setup()

    window.show_view(game)
    window.run()


if __name__ == "__main__":
    main()
