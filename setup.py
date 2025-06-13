from setuptools import setup, find_packages

setup(
    name='permission_cloner',
    version='0.0.1',
    description='App to clone permissions between roles in ERPNext',
    author='jagdeepsinghvirdi',
    author_email='your@email.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['frappe'],
)
