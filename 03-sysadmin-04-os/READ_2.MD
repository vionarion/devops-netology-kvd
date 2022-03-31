в службу будут передаются дополнительные опции с помощью 

ExecStart=/bin/bash -c 'v=%i; USE_GPU=$${v%:*} exec /bin/mycommand'

ExecStart=/usr/bin/myservice -C /etc/myservice/%i.conf


vagrant@vagrant:/etc/systemd/system$ cat /etc/systemd/system/node_exporter.service
[Unit]
Description=Node Exporter
 
[Service]
ExecStartPre=
ExecStart=/opt/node_exporter/node_exporter
EnvironmentFile=/etc/default/node_exporter
 
[Install]
WantedBy=default.target