package Creational.FactoryMethod;

public class VeggieBurgerRestaurant extends Restaurant {
    @Override
    public Burger createBurger() {
        System.out.println("Creating veggie burger...");
        return new VeggieBurger();
    }
}
