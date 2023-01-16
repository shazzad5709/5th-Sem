from MazeBuilder import MazeBuilder
from Maze import Maze
from Room import Room
from Wall import Wall
from Door import Door

class StandardMazeBuilder(MazeBuilder):
    def __init__(self):
        self._maze = None

    def build_maze(self):
        self._maze = Maze()

    def build_room(self, room_number):
        if self._maze.get_room(room_number) is None:
            room = Room(room_number)
            self._maze.add_room(room)
            room.set_side('north', Wall())
            room.set_side('south', Wall())
            room.set_side('east', Wall())
            room.set_side('west', Wall())

    def build_door(self, room_from, room_to):
        room1 = self._maze.get_room(room_from)
        room2 = self._maze.get_room(room_to)
        door = Door(room1, room2)
        room1.set_side('east', door)
        room2.set_side('west', door)

    def get_maze(self):
        return self._maze