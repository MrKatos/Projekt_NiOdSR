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









Camera Control – ROS2

Projekt umożliwia sterowanie TurtleBotem na podstawie kliknięcia
w czarne okno.

 Wymagania
- ROS2 Humble
- turtlebot3
- cv_bridge
- OpenCV

 Instalacja
cd ~/ros2_ws/src
git clone https://github.com/MrKatos/Projekt_NiOdSR
cd ~/ros2_ws
colcon build --packages-select camera_control
source install/setup.bash

 Uruchomienie
ros2 launch camera_control turtle_launch.py

Sterowanie
 klik powyżej środka - jazda w prawo
 klik poniżej środka - jazda w lewo

