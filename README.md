# ROS2 Robot Control 🤖🚧

## Opis projektu

Projekt został zrealizowany w środowisku **ROS2** i stanowi interfejs do sterowania zolwikiem z wykorzystaniem kliknięcia myszką.
Celem projektu było stworzenie Node'a, który steruje TurtleSIM w środowisku ROS2.

---

## Funkcjonalność 
- uruchomienie własnego Node'a sterującego robotem,
- sterowanie robotem poprzez kliknięcie myszy w czarny ekran
- publikacja kodu w repozytorium GitHub wraz z dokumentacją.

---

## Instalacja

cd ~/ros2_ws/src

git clone https://github.com/MrKatos/Projekt_NiOdSR

cd ~/ros2_ws

colcon build --packages-select camera_control

source install/setup.bash

---

## Uruchomienie
 
ros2 launch camera_control turtle_launch.py

---

## DockerFile
### Budowanie obrazu:
cd ~/ros2_ws/src/camera_control 

docker biuld camera_control_obraz
### Urochomianie konteneru:

xhost +

docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw --volume [PATH]:[IMAGE_PATH] [ID] bash

xhost -






### Sterowanie
- klik powyżej środka - jazda w prawo
- klik poniżej środka - jazda w lewo
 
<img width="1207" height="553" alt="image" src="https://github.com/user-attachments/assets/8a931b9d-38ba-49c5-a88a-bcc99045ab4d" />

