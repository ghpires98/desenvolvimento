# desenvolvimento

# Atualização de Requeriments

     pip freeze > requeriments.txt


     docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=xxxxxxxxx -p 3306:3306 -v mysqlVolume:/var/lib/mysql -d mysql:latest