from setuptools import setup, find_packages
# setuptools allows creating packages from the folder containing __init__.py

setup(
    name="src",  # give some name to your package
    version="0.0.1",
    description="its a wine Q package", 
    author="jakhmodp9c", 
    packages=find_packages(), # finds all the packages in working directory
    license="MIT"
)

# run command - "pip install -e ." to install this package.