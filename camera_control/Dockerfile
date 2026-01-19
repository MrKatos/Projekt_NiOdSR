FROM ros:humble

# Instalacja OpenCV i zależności (Zadanie 1)
RUN apt-get update && apt-get install -y \
    python3-opencv \
    ros-humble-cv-bridge \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app/src/camera_control

# Budowanie środowiska (Punkt 5 instrukcji)
RUN . /opt/ros/humble/setup.sh && colcon build

# Automatyczne uruchomienie projektu
CMD ["bash", "-c", "source install/setup.bash && ros2 launch camera_control turtle_launch.py"]
