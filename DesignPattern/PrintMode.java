public abstract class PrintMode {
    int pageNo;
    int pageSize;
    String orientation;
    int colorIntensity;
    float cost;

    abstract void printMode(PrintMode x);
}