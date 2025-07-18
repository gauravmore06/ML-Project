from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    HYPEN_E_DOT = '-e .'

    requirements = []

    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name="mlproject",
    version="0.0.1",
    author='Gaurav',
    author_email='gauravmore0206@gmail.com',
    packages=find_packages(),
    requires= get_requirements('requirements.txt')
)