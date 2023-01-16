from StandardMazeBuilder import StandardMazeBuilder

class MazeGame:
    def create_maze(self, builder):
        builder.build_maze()
        builder.build_room(1)
        builder.build_room(2)
        builder.build_door(1, 2)
        return builder.get_maze()

if __name__ == '__main__':
    builder = StandardMazeBuilder()
    game = MazeGame()
    maze = game.create_maze(builder)
    # do something with the maze