from setuptools import setup, find_packages

setup(
    name='item_reservation',
    version='0.0.1',
    description='Item Reservation App for Frappe',
    author='Neotec Admin',
    author_email='hostadmin@neotechiss.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['frappe'],
)
