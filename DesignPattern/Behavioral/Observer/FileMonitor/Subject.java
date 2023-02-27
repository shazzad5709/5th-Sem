package DesignPattern.Behavioral.Observer.FileMonitor;

import java.util.ArrayList;

public abstract class Subject {
    ArrayList<Observer> observersArrayList = new ArrayList<>();
    public abstract void registeredObserver(Observer observers);
    public abstract void unregisteredObserver(Observer observers);
    public abstract void notifyy(String fileName, String changeType, String changeTime);
}
