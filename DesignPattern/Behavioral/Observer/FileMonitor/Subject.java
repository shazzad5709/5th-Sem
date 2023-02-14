package DesignPattern.Behavioral.Observer.FileMonitor;

import java.io.IOException;

public interface Subject {
    public void register(Observer o);
    public void unregister(Observer o);
    public void notifyObserver();
    public void monitor() throws IOException, InterruptedException;
}
