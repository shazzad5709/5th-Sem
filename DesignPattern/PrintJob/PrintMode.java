public abstract class PrintMode {
    Integer pageNo;
    Integer pageSize;
    String orientation;
    Integer colorIntensity;
    float cost;

    abstract void printMode(PrintMode x);
}