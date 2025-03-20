#!/bin/bash

# Cambiar a la ruta absoluta de Kafka
cd "/usr/local/kafka/" || { echo "No se pudo acceder al directorio de Kafka"; exit 1; }

echo "BIENVENIDO AL PANEL DE KAFKA!"
echo "         MENÚ PRINCIPAL      "
echo "============================="
echo "1) Crear Tema"
echo "2) Guardar Temas"
echo "3) Listar Tema"
echo "4) Abrir Emisor"
echo "5) Abrir Consumidor"
echo "6) Salir"
echo "============================="
echo -n "Selecciona una opción [1-4]: "

read -r option

case $option in
    1)
        echo "Crear Topic"
        echo "Escribe el nombre del topic que quieres crear: "
        read -r nombre
        ./bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic "$nombre"
        ./bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
        ;;
    2)
        echo "Guardar Temas..."
        ./bin/kafka-topics.sh --bootstrap-server localhost:9092 --list > topics.txt
	cat topics.txt
        ;;
    3)
        echo "Listando Topics del Sistema"
	./bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
        ;;
    4) echo "Desplegando Productor..."
	echo "Escribe el nombre del topic"
        read -r nombreTopic
	./bin/kafka-console-producer.sh --broker-list localhost:9092 --topic "$nombreTopic"
	;;
    5) echo "Desplegando Consumidor..."
	echo "Escribe el nombre del Topic"
       	read -r nombreTopic
       	./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic "$nombreTopic" --from-beginning
	;;
    6)
        echo "Saliendo..."
        exit 0
        ;;
    *)
        echo "Opción no válida"
        ;;
esac


