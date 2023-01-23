public class Client {
    public static void main(String[] args) {
        // Create a factory
        WidgetFactory factory = new MotifWidgetFactory();
        // Create a window using the factory
        Window window = factory.createWindow();
        // Create a scroll bar using the factory
        ScrollBar scrollBar = factory.createScrollBar();
    }
}
