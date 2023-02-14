package DesignPattern.Behavioral.Observer.Test;

import java.util.ArrayList;
import java.util.List;

public abstract class Subject {
    private List<Observer> observers=new ArrayList<>();

    public void attach(Observer observer){
        observers.add(observer);
    }
    public void detach(Observer observer){
        observers.remove(observer);
    }

    public void notify(String fileName, String changeType, String changeTime){
        for(Observer observer:observers){
            System.out.println("Observer list");
            observer.Update(fileName, changeType, changeTime);
        }
    }
}
