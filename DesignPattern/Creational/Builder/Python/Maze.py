class Maze:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.number] = room

    def get_room(self, room_number):
        return self.rooms.get(room_number)