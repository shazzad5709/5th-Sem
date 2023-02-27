package DesignPattern.Behavioral.Observer.FileMonitor;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        ConcreteSubject monitor = new ConcreteSubject("a.txt", ".");

        ConcreteObserver observer1 = new ConcreteObserver();
        ConcreteObserver observer2 = new ConcreteObserver();
        monitor.registeredObserver(observer1);
        monitor.registeredObserver(observer2);

        monitor.getUpdate();
    }
}
