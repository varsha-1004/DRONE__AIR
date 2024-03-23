from setuptools import setup

package_name = 'test_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='xlr8wins',
    maintainer_email='varsha.nagarajan@gmail.com',
    description='practice packages to do',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = test_pandee.my_node:main'
        ],
    },
)
