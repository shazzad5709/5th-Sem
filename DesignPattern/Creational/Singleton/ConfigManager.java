package Creational.Singleton;

import java.util.HashMap;
import java.util.Map;

class ConfigManager {

    public static ConfigManager instance;

    private Map<String, String> configMap = new HashMap<String, String>() {{
        put("host", "internal.db");
        put("port", "5500");
        put("user", "admin");
        put("password", "#Admin#");
    }};

    public String update(String key, String value) {
        return configMap.put(key, value);
    }

    public String get(String key) {
        return configMap.get(key);
    }

    private ConfigManager() {

    }

    public static synchronized ConfigManager getInstance() {
        if (instance==null)
            instance = new ConfigManager();
            
        return instance;
    }

}

