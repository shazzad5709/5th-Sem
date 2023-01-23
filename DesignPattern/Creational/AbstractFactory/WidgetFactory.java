public abstract class WidgetFactory {
    public static WidgetFactory createFactory(String factoryName) {
        WidgetFactory factory = null;
        if (factoryName.equals("Motif")) {
            factory = new MotifWidgetFactory();
        } else if (factoryName.equals("PM")) {
            factory = new PMWidgetFactory();
        }
        return factory;
    }
    public abstract Window createWindow();
    public abstract ScrollBar createScrollBar();
}