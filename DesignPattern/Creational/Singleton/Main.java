package Creational.Singleton;

public class Main {
    public static void main(String[] args) {
        ConfigManager configManager1 = ConfigManager.getInstance();
        ConfigManager configManager2 = ConfigManager.getInstance();

        configManager1.update("password", "#NewPass");

        String password = configManager2.get("password");
        System.out.println(password);
    }
}
