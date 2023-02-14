package DesignPattern.Behavioral.Observer.Test;

public class ConcreteObserver extends Observer{
    private String observerName;

    public ConcreteObserver(String observerName){
        this.observerName=observerName;
    }
    @Override
    public void Update(String fileName, String changeType, String changeTime){
        System.out.print("Observer: " +observerName);
        System.out.println(" The file: "+fileName+" is changed whose type: "+changeType+" and time: "+changeTime);
    }
}
