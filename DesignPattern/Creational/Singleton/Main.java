package Creational.Singleton;

public class Main {
    public static void main(String[] args) {
        System.out.println();
        System.out.println(Singleton.getInstance("ABC"));
        Singleton singleton = Singleton.getInstance("XYZ");
        System.out.println(singleton);
        System.out.println(singleton.getData());

    }
}
