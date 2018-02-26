from subprocess import call


# Descargamos e instalamos el node
call("sudo lxc-attach --clear-env  -n s1 -- bash -c \"curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -\"", shell=True);
call("sudo lxc-attach --clear-env  -n s1 -- sudo apt-get install -y nodejs", shell=True);

call("sudo lxc-attach --clear-env  -n s2 -- bash -c \"curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -\"", shell=True);
call("sudo lxc-attach --clear-env  -n s2 -- sudo apt-get install -y nodejs", shell=True);

call("sudo lxc-attach --clear-env  -n s3 -- bash -c \"curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -\"", shell=True);
call("sudo lxc-attach --clear-env  -n s3 -- sudo apt-get install -y nodejs", shell=True);

# Configuracion de los servidores
#Primero exportamos la variable de entorno DATABASE_URL de la base de datos
#Despues descargamos el CRM del Github, instalamos las dependencias y la utilidad forever, para poder arrancar el servidor CRM en background
call("sudo lxc-attach --clear-env -n s1 -- bash -c \"export DATABASE_URL=postgres://crm:xxxx@10.1.4.31:5432/crm; cd /root; git clone https://github.com/CORE-UPM/CRM_2017; cd /root/CRM_2017; npm install; npm install forever; \"", shell=True);
call("sudo lxc-attach --clear-env -n s2 -- bash -c \"export DATABASE_URL=postgres://crm:xxxx@10.1.4.31:5432/crm; cd /root; git clone https://github.com/CORE-UPM/CRM_2017; cd /root/CRM_2017; npm install; npm install forever; \"", shell=True);
call("sudo lxc-attach --clear-env -n s3 -- bash -c \"export DATABASE_URL=postgres://crm:xxxx@10.1.4.31:5432/crm; cd /root; git clone https://github.com/CORE-UPM/CRM_2017; cd /root/CRM_2017; npm install; npm install forever; \"", shell=True);


#Creamos el directorio public/uploads donde se copiaran las imagenes subidas
#Ejecutamos el comando mount para poder acceder al sistema de ficheros exportado
#por los nas desde los servidores web.
call("sudo lxc-attach --clear-env -n s1 -- bash -c \"export DATABASE_URL=postgres://crm:xxxx@10.1.4.31:5432/crm; cd /root/CRM_2017; mkdir public/uploads; mount -t glusterfs 10.1.4.21:/nas public/uploads; ./node_modules/forever/bin/forever start ./bin/www  \"", shell=True);
call("sudo lxc-attach --clear-env -n s2 -- bash -c \"export DATABASE_URL=postgres://crm:xxxx@10.1.4.31:5432/crm; cd /root/CRM_2017; mkdir public/uploads; mount -t glusterfs 10.1.4.21:/nas public/uploads; ./node_modules/forever/bin/forever start ./bin/www  \"", shell=True);
call("sudo lxc-attach --clear-env -n s3 -- bash -c \"export DATABASE_URL=postgres://crm:xxxx@10.1.4.31:5432/crm; cd /root/CRM_2017; mkdir public/uploads; mount -t glusterfs 10.1.4.21:/nas public/uploads; ./node_modules/forever/bin/forever start ./bin/www  \"", shell=True);

#Migrate y seed solo en s1
call("sudo lxc-attach --clear-env -n s1 -- bash -c \"export DATABASE_URL=postgres://crm:xxxx@10.1.4.31:5432/crm; cd /root/CRM_2017; npm run-script migrate_local; npm run-script seed_local  \"", shell=True);










