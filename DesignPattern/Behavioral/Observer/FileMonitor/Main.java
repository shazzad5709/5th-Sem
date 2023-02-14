package DesignPattern.Behavioral.Observer.FileMonitor;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        Subject monitor = new ConcreteSubject();

        Observer observer1 = new ConcreteObserver(monitor);
        Observer observer2 = new ConcreteObserver(monitor);
        Observer observer3 = new ConcreteObserver(monitor);
        Observer observer4 = new ConcreteObserver(monitor);
        Observer observer5 = new ConcreteObserver(monitor);

        monitor.monitor();

        observer1.draw();
        observer2.draw();
        observer3.draw();
        observer4.draw();
        observer5.draw();
    }
}
