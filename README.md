# Folder structure
```
grafana-influxdb-telegraf
|   configuration.env
|   docker-compose.yml
|   README.md
|
└───grafana
|   |
|   └───dashboards
|           dashboards.json
|
└───publisher
|       pub.py
|
└───telegraf
    |
    └───config
    |       sample.conf
    |       telegraf.conf
```

# Environment information
- OS: Ubuntu 18.04 LTS

# Softwares
- Docker Engine: lastest version
- Docker Compose: v1.29.2, build 5becea4c

# Services in docker
- grafana: v8.5.4
- influxdb: v1.8 version (v1.x)
- telegraf: latest version