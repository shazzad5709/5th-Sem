package Creational.FactoryMethod;

public class BeefBurgerRestaurant extends Restaurant {
    @Override
    public Burger createBurger() {
        System.out.println("Creating beef burger...");
        return new BeefBurger();
    }
}
