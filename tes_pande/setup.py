from setuptools import setup

package_name = 'tes_pande'

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
    description='let us test pandee',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'talker = tes_pande.publisher_member_function:main',
		'listener = tes_pande.subscriber_member_function:main',
        ],
    },
)
