import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'shikanoko_markov_statemachine'

data_files = []
data_files.append(
    ("share/ament_index/resource_index/packages", ["resource/" + package_name])
)
data_files.append(("share/" + package_name, ["package.xml"]))


def package_files(directory, data_files):
    for path, directories, filenames in os.walk(directory):
        for filename in filenames:
            data_files.append(
                (
                    "share/" + package_name + "/" + path,
                    glob(path + "/**/*.*", recursive=True),
                )
            )
    return data_files

# Add directories
data_files = package_files("video", data_files)

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='humble-gai',
    maintainer_email='humble-gai@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'shikanoko_markov_statemachine=shikanoko_markov_statemachine.shikanoko_markov_statemachine:main'
        ],
    },
)
