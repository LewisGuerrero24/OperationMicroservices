#!/bin/bash

CONFIG_FILE="./topics-config.txt"
CONTAINER_NAME="system-control-and-operations-process-events-kafka-1"
DOCKER_COMPOSE_PATH="."


# Función para verificar si el contenedor está en ejecución
# is_container_running() {
#     sudo docker ps --format "{{.Names}}" | grep -q "$CONTAINER_NAME"
# }

echo "BIENVENIDO AL PANEL DE KAFKA!"
echo "         MENÚ PRINCIPAL      "
echo "============================="
echo "1) Levantar Contenedores"
echo "2) Ver contenedores en ejecución"
echo "3) Crear Tema"
echo "4) Guardar Temas"
echo "5) Crear temas desde el archivo txt"
echo "6) Listar temas"
echo "7) Abrir Emisor"
echo "8) Abrir Consumidor"
echo "10) Salir"
echo "============================="
echo -n "Selecciona una opción [1-8]: "

read -r option

case $option in
    1)    
        echo "🔄 Levantando contenedores de Docker..."
        cd "$DOCKER_COMPOSE_PATH" || { echo "❌ No se pudo acceder al directorio del proyecto"; exit 1; }
        sudo docker compose up -d
        echo "✅ Contenedores levantados exitosamente."
        ;;

    2) 
        echo "🔎 Verificando contenedores de Docker en ejecución..."
        sudo docker ps 
        ;;

    3)
        echo "📝 Creando tema..."
        echo "Escribe el nombre del topic que quieres crear: "
        read -r nombre
        sudo docker exec -it "$CONTAINER_NAME" /usr/bin/kafka-topics --create --topic "$nombre" --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 
        echo "✅ Tema creado exitosamente."
        ;;

    4)
        echo "Guardar temas existentes..."
        sudo docker exec -it "$CONTAINER_NAME" /usr/bin/kafka-topics --bootstrap-server localhost:9092 --list | \
        while read -r topic; do
            # Verifica si el tópico ya está en el archivo, si no, lo agrega
            grep -qxF "$topic" topics-config.txt || echo "$topic" >> topics-config.txt
        done
        echo "✅ Tópicos guardados exitosamente."
        cat topics-config.txt
        ;;

    5)
        echo "🔍 Verificando y creando temas desde el archivo '$CONFIG_FILE'..."
        if [ ! -f "$CONFIG_FILE" ]; then
            echo "❌ El archivo '$CONFIG_FILE' no existe."
            exit 1
        fi

        # Obtener los temas existentes en el contenedor
        EXISTING_TOPICS=$(sudo docker exec "$CONTAINER_NAME" /usr/bin/kafka-topics --bootstrap-server localhost:9092 --list)

        while IFS= read -r topic; do
            # Limpiar nombre del tópico eliminando espacios y caracteres no deseados
            topic=$(echo "$topic" | tr -d '\r' | tr -d '\n' | xargs)

            # Verificar si el tópico ya existe
            if echo "$EXISTING_TOPICS" | grep -qxF "$topic"; then
                echo "✅ El tópico '$topic' ya existe."
            else
                echo "➕ Creando tópico '$topic'..."
                sudo docker exec "$CONTAINER_NAME" /usr/bin/kafka-topics --create --topic "$topic" --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
                echo "✅ Tópico '$topic' creado exitosamente."
            fi
        done < "$CONFIG_FILE"
        ;;


    6)
        echo "📝 Listando temas..."
        sudo docker exec -it "$CONTAINER_NAME" /usr/bin/kafka-topics --bootstrap-server localhost:9092 --list
        ;;


    7)  
        echo "Desplegando Productor..."
	    echo "Escribe el nombre del topic"
        read -r nombreTopic
	    sudo docker exec -it "$CONTAINER_NAME" /usr/bin/kafka-console-producer --broker-list localhost:9092 --topic "$nombreTopic"
	;;


    8)  
        echo "Desplegando Consumidor..."
	    echo "Escribe el nombre del Topic"
       	read -r nombreTopic
       	sudo docker exec -it "$CONTAINER_NAME" /usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic "$nombreTopic" --from-beginning
	;;
    9)
        echo "Saliendo..."
        exit 0
        ;;
    *)
        echo "Opción no válida"
        ;;
esac


