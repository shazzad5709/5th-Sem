package DesignPattern.Behavioral.Observer.Test;


public class Main {
    public static void main(String[] args) {

        ConcreteSubject subject=new ConcreteSubject("observe.txt", ".");

        ConcreteObserver observer1=new ConcreteObserver("1");
        ConcreteObserver observer2=new ConcreteObserver("2");

        subject.attach(observer1);
        subject.attach(observer2);

        try{
            subject.getUpdate();
        }catch(Exception e){
            e.printStackTrace();
        }

    }
}