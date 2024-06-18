## Start with the official Maven image to build your application
#FROM maven:3.8.4-openjdk-11-slim AS build
#COPY src /home/app/src
#COPY pom.xml /home/app
#RUN mvn -f /home/app/pom.xml clean package
#
## Use OpenJDK image that will also include Python
#FROM openjdk:11-jre-slim as runtime
#
## Install Python
#RUN apt-get update && apt-get install -y python3 python3-pip
#
## Set the working directory for the application
#WORKDIR /app
#
## Copy the built jar file from the build stage
#COPY --from=build /home/app/target/*.jar /app/app.jar
#
## Copy your Python script to the container
#COPY ./path-to-your-python-script/Combined_code_village.py /app/Combined_code_village.py
#
## Expose the port that your Spring app uses
#EXPOSE 8080
#
## Command to run your application
#ENTRYPOINT ["java", "-jar", "/app/app.jar"]
# Stage 1: Build the JAR file
FROM maven:3.8.4-openjdk-17 AS build

# Set the working directory
WORKDIR /app

# Copy the pom.xml and download dependencies
COPY pom.xml .
RUN mvn dependency:go-offline

# Copy the source code and example folder, then build the application
COPY src ./src
COPY All_codes ./All_codes
COPY mixedd ./mixedd
#COPY "negative maps" ./negative_maps
COPY py_outputs ./py_outputs
COPY radar ./radar

RUN mvn clean package -DskipTests

# Stage 2: Create the Docker image
FROM openjdk:17-jdk-alpine

# Install Python
RUN apk add --no-cache python3 py3-pip

# Set the working directory
WORKDIR /app

# Copy the JAR file from the build stage
COPY --from=build /app/target/*.jar /app.jar

# Specify the command to run your application
ENTRYPOINT ["java", "-jar", "/app.jar"]
