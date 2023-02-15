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
    }
}
