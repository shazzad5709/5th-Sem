package DesignPattern.Behavioral.Observer.Test;


import java.io.IOException;
import java.nio.file.*;
import java.util.Date;

public class ConcreteSubject extends Subject{
    private String fileName;
    private String path;

    public ConcreteSubject(String fileName, String path){
        this.fileName=fileName;
        this.path=path;
    }
    public void getUpdate() throws IOException, InterruptedException {
        WatchService watchService= FileSystems.getDefault().newWatchService();
        Path dirPath= Paths.get(path);
        System.out.println(dirPath);
        dirPath.register(watchService, StandardWatchEventKinds.ENTRY_MODIFY);

        while(true){
            WatchKey key=watchService.take();

            for(WatchEvent<?> event: key.pollEvents()){
                String eventFileName = event.context().toString();

                if(eventFileName.equals(fileName)){
                    String changeType=event.kind().name();
                    String changeTime=new Date().toString();

                    //notify observer
                    notify(fileName, changeType, changeTime);
                }
            }

            boolean valid=key.reset();

            if(!valid){
                break;
            }
        }
    }
}