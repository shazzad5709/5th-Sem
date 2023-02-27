package DesignPattern.Behavioral.Observer.FileMonitor;

public class ConcreteObserver implements Observer{

    @Override
    public void update(String fileName, String changeType, String changeTime) {
        System.out.println("Changed file: "+fileName+"Changing type: "+changeType+"Changing time"+changeTime);
    }
}
