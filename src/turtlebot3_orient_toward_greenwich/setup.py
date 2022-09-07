from setuptools import setup
from glob import glob
import os
package_name = 'turtlebot3_orient_toward_greenwich'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hazem',
    maintainer_email='hazemahmedfreestyle@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'Turtlebot = turtlebot3_orient_toward_greenwich.Turtlebot:main ',
                             'Robot_interface = turtlebot3_orient_toward_greenwich.Robot_interface:main' 

        ],
    },
)
