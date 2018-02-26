from subprocess import call

#Para crear el cluster de servidores de disco. 
#Anadimos los servidores al cluster
call("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 10.1.4.22", shell=True);
call("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 10.1.4.23", shell=True);

#Creamos en nas1 el directorio que se sincronizara con el res
call("sudo lxc-attach --clear-env -n nas1 -- mkdir /root/nas",shell=True); 

#Creamos el volumen con tres servidores que replican la info
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume create nas replica 3 transport tcp 10.1.4.21:/root/nas 10.1.4.22:/root/nas 10.1.4.23:/root/nas force", shell=True);

#Arrancamos el volumen
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume start nas",shell=True);

#Para agilizar la recuperacion del volumen ante caidas de uno de los servidores
call("sudo lxc-attach --clear-env -n nas1 -- gluster volume set nas network.ping-timeout 5", shell=True);
call("sudo lxc-attach --clear-env -n nas2 -- gluster volume set nas network.ping-timeout 5", shell=True);
call("sudo lxc-attach --clear-env -n nas3 -- gluster volume set nas network.ping-timeout 5", shell=True);
