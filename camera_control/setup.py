from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'camera_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # Rejestracja paczki w systemie ROS2
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Instalacja plików launch, aby były widoczne dla ros2 launch
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kacper',
    maintainer_email='kacper.wiet1@gmail.com',
    description='Projekt sterowania robotem UR5 za pomocą interfejsu graficznego',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'interface_node = camera_control.interface_node:main',
        'turtle_controller = camera_control.turtle_controller:main',
    ],
  },
)
