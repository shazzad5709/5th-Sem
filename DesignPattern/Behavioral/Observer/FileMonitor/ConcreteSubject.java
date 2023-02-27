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

class ConcreteSubject extends Subject{
    private String fileName;
    private String path;
    @Override
    public void registeredObserver(Observer observer) {
        observersArrayList.add(observer);
    }

    @Override
    public void unregisteredObserver(Observer observer) {
        observersArrayList.remove(observer);
    }

    @Override
    public void notifyy(String fileName, String changeType, String changeTime) {
        for (Observer itr: observersArrayList) {
            itr.update(fileName,changeType,changeTime);
        }
    }
    public ConcreteSubject(String fileName, String path){
        this.fileName=fileName;
        this.path=path;
    }
    public void getUpdate() throws IOException, InterruptedException {
        String pathStr = ".";
        Path path = Paths.get(pathStr);
        System.out.println(path);
        try (final WatchService watchService = FileSystems.getDefault().newWatchService()) {
            final WatchKey watchKey = path.register(watchService, StandardWatchEventKinds.ENTRY_MODIFY);
            while (true) {
                final WatchKey wk = watchService.take();
                for (WatchEvent<?> event : wk.pollEvents()) {
                    final Path changed = (Path) event.context();
                    System.out.println(changed);
                    System.out.println(event.kind());
                    System.out.println(changed);
                    if (changed.endsWith("a")) {
                        String timeStamp = new SimpleDateFormat("yyyyMMdd_HHmmss").format(Calendar.getInstance().getTime());
                        System.out.println("My file has changed at "+timeStamp);
                    }
                }
                // reset the key
                boolean valid = wk.reset();
                if (!valid) {
                    System.out.println("Key has been unregistered");
                }
            }
        } catch(Exception err){
            err.printStackTrace();
        }
    }
}
