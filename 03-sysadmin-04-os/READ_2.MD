в службу будут передаются дополнительные опции с помощью 

ExecStart=/bin/bash -c 'v=%i; USE_GPU=$${v%:*} exec /bin/mycommand'