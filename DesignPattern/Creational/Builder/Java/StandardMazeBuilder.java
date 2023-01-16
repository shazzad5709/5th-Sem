package Creational.Builder.Java;

public class StandardMazeBuilder extends MazeBuilder {
    public StandardMazeBuilder() {
        super();
    }

    public void buildMaze() {
        this.currentMaze = new Maze();
    }

    public void buildRoom(int roomNumber) {
        if (this.currentMaze.getRoom(roomNumber) == null) {
            Room room = new Room(roomNumber);
            this.currentMaze.addRoom(room);
            room.setSide(Direction.NORTH, new Wall());
            room.setSide(Direction.SOUTH, new Wall());
            room.setSide(Direction.EAST, new Wall());
            room.setSide(Direction.WEST, new Wall());
        }
    }

    public void buildDoor(int roomFrom, int roomTo) {
        Room room1 = this.currentMaze.getRoom(roomFrom);
        Room room2 = this.currentMaze.getRoom(roomTo);
        Door door = new Door(room1, room2);
        room1.setSide(Direction.EAST, door);
        room2.setSide(Direction.WEST, door);
    }

    public Maze getMaze() {
        return this.currentMaze;
    }
}
