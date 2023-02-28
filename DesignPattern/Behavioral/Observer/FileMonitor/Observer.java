package DesignPattern.Behavioral.Observer.FileMonitor;

public interface Observer {
    public void update(String fileName, String changeType, String changeTime);

}
