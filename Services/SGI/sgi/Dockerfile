# Usa la versión de Node 23.7.0
FROM node:23.7.0-alpine

# Establece el directorio de trabajo
WORKDIR /app

# Copia package.json y package-lock.json
COPY package*.json ./

# Instala dependencias
RUN npm install

# Copia el código fuente
COPY . .

# Expone el puerto en el que corre NestJS (por defecto 3000)
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["npm", "run", "start"]

