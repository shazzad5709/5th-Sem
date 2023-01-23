public class MotifWidgetFactory extends WidgetFactory{
    public Window createWindow() {
        return new MotifWindow();
    }
    public ScrollBar createScrollBar() {
        return new MotifScrollBar();
    }
}
