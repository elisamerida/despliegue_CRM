import subprocess

#Configuramos el lb para que ejecute balancee el trafico entre los 3 servidores
subprocess.call("sudo lxc-attach --clear-env -n lb -- sudo xr -dr -S --verbose --server tcp:0:80 --backend 10.1.3.11:3000 --backend 10.1.3.12:3000 --backend 10.1.3.13:3000 --web-interface 0:8001", shell=True);
