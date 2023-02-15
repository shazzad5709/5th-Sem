package DesignPattern.Behavioral.Observer.FileMonitor;

import java.util.ArrayList;
import java.util.List;
import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardWatchEventKinds;
import java.nio.file.WatchEvent;
import java.nio.file.WatchKey;
import java.nio.file.WatchService;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class ConcreteSubject implements Subject {
    private List<Observer> observers;
    private String fileName = "test";
    private String pathStr = ".";
    private String time = null;

    public ConcreteSubject() {
        observers = new ArrayList<Observer>();
    }

    @Override
    public void register(Observer newObserver) {
        this.observers.add(newObserver);

    }

    @Override
    public void unregister(Observer deleteObserver) {
        int observerIdx = observers.indexOf(deleteObserver);
        System.out.println("Observer " + (observerIdx + 1) + " deleted");
        this.observers.remove(deleteObserver);
    }

    @Override
    public void notifyObserver() {
        for (Observer observer : observers) {
            observer.update(this);
        }

    }

    @Override
    public void monitor() throws IOException, InterruptedException {
        Path path = Paths.get(pathStr);
        try (final WatchService watchService = FileSystems.getDefault().newWatchService()) {
            final WatchKey watchKey = path.register(watchService, StandardWatchEventKinds.ENTRY_MODIFY);
            while (true) {
                final WatchKey wk = watchService.take();
                for (WatchEvent<?> event : wk.pollEvents()) {
                    final Path changed = (Path) event.context();
                    System.out.println(changed);

                    if (changed.endsWith(fileName)) {
                        Calendar cal = Calendar.getInstance();
                        SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss");
                        time = sdf.format(cal.getTime());
                        notifyObserver();
                    }
                }

                boolean valid = wk.reset();
                if (!valid) {
                    System.out.println("Key has been unregisterede");
                }
            }
        }
    }

    public String getFileName() {
        return this.fileName;
    }

    public String getTime() {
        return this.time;
    }
}
