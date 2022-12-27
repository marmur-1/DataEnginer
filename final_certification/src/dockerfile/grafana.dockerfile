FROM grafana/grafana:9.3.2
COPY ./grafana/dashboard.json /etc/grafana/dashboards/dashboard.json
COPY ./grafana/dashboard.yml /etc/grafana/provisioning/dashboards/dashboard.yml
COPY ./grafana/datasource.yml /etc/grafana/provisioning/datasources/datasource.yml