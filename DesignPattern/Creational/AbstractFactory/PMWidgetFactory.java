public class PMWidgetFactory extends WidgetFactory{
    public Window createWindow() {
        return new PMWindow();
    }
    public ScrollBar createScrollBar() {
        return new PMScrollBar();
    }
}
