from setuptools import setup, find_packages

setup(
    name='pyodre',
    version='1.0.0',
    packages=find_packages(),  # Encuentra todos los paquetes automáticamente
    install_requires=["rdflib>=7.0.0", "jinja2>=3.1.2"],
    author='Andrea Cimmino',
    author_email='andreajesus.cimmino@upm.es',
    description='Open Digital Rights Enforcement Framework python implementation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ODRE-Framework/odre-python',
    classifiers=[
         "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.9",
    ],

    python_requires='>=3.9',
)