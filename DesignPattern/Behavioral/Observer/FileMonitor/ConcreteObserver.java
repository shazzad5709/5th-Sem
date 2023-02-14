package DesignPattern.Behavioral.Observer.FileMonitor;

public class ConcreteObserver implements Observer {
    private static int observerIDTracker = 0;
    private int observerID;
    private Subject fileSubject;

    public ConcreteObserver(Subject fileSubject) {
        this.fileSubject = fileSubject;
        this.observerID = ++observerIDTracker;
        System.out.println("New Observer " + this.observerID);
        fileSubject.register(this);
    }

    @Override
    public void update(Subject subject) {
        this.fileSubject = (ConcreteSubject)subject;
        System.out.println("Changes: " + "Observer " + this.observerID + " --- " + ((ConcreteSubject) fileSubject).getTime() + " --- " + ((ConcreteSubject) fileSubject).getFileName() + " was modified");
    }

    public void draw() {
        System.out.println("Observer " + this.observerID + " is drawing");
    }
    
}
