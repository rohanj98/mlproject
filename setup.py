from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    Function to return the list of libraries
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(
name = 'mlproject',
version='0.0.1',
author='Rohan',
author_email='rohanjadhav1@protonmail.com',
packages=find_packages(),
#install_requires=['pandas','numpy','seaborn']
install_requires=get_requirements('requirements.txt')
)