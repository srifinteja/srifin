# Start with the official Maven image to build your application
FROM maven:3.8.4-openjdk-11-slim AS build
COPY src /home/app/src
COPY pom.xml /home/app
RUN mvn -f /home/app/pom.xml clean package

# Use OpenJDK image that will also include Python
FROM openjdk:11-jre-slim as runtime

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory for the application
WORKDIR /app

# Copy the built jar file from the build stage
COPY --from=build /home/app/target/*.jar /app/app.jar

# Copy your Python script to the container
COPY ./path-to-your-python-script/Combined_code_village.py /app/Combined_code_village.py

# Expose the port that your Spring app uses
EXPOSE 8080

# Command to run your application
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
