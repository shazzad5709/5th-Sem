package Creational.Builder.Java;

abstract class MazeBuilder {
    protected Maze currentMaze;
    public MazeBuilder() {
        this.currentMaze = null;
    }
    
    public abstract void buildMaze();
    public abstract void buildRoom(int roomNumber);
    public abstract void buildDoor(int roomFrom, int roomTo);
    public abstract Maze getMaze();
}
