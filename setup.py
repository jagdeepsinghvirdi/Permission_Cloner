
from setuptools import setup, find_packages

setup(
    name='permission_cloner',
    version='0.0.1',
    description='Tool to copy role permissions',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['frappe']
)
