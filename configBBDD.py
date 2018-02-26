from subprocess import call

#Actualizacio de paquetes e instalacion del sistema de gestion de bases de datos relacional
call("sudo lxc-attach --clear-env -n bbdd -- apt update", shell=True);
call("sudo lxc-attach --clear-env -n bbdd -- apt -y install postgresql", shell=True);

#Modificacion del fichero de configuracion de la base de datos para que escuche en la direccion IP indicada en el escenario
cmd="sudo lxc-attach --clear-env -n bbdd -- bash -c \"echo 'listen_addresses='\\\'10.1.4.31\\\''' >> /etc/postgresql/9.6/main/postgresql.conf\" "
call(cmd, shell=True);

#Modificacion del fichero que controla la autenticacion del cliente.
#Permitimos los intentos de conexion TCP/IP de todas las bases de datos y todos los usuarios de manera incondicional en el rango de direcciones IP indicado.
cmd = "sudo lxc-attach --clear-env -n bbdd -- bash -c \"echo 'host all all 10.1.4.0/24 trust' >> /etc/postgresql/9.6/main/pg_hba.conf\" "
call(cmd, shell=True);

#Crear usuario en la base de datos a traves de la consola interactiva 
cmd = "sudo lxc-attach --clear-env -n bbdd -- bash -c \"echo 'CREATE USER crm with PASSWORD '\\\"'xxxx'\\\"';' | sudo -u postgres psql \" "
call(cmd, shell=True);
#Crear base de datos a traves de la consola interactiva
cmd = "sudo lxc-attach --clear-env -n bbdd -- bash -c \"echo 'CREATE DATABASE crm;' | sudo -u postgres psql\" "
call(cmd, shell=True)
#Garantizar todos los privilegios al usuario en la base de datos a traves de la consola interactiva
cmd = "sudo lxc-attach --clear-env -n bbdd -- bash -c \"echo 'GRANT ALL PRIVILEGES ON DATABASE crm to crm;' | sudo -u postgres psql\" "
call(cmd, shell=True)
#Reiniciar para que se apliquen los cambios
cmd = "sudo lxc-attach --clear-env -n bbdd -- systemctl restart postgresql"
call(cmd, shell=True)
