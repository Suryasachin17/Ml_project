from setuptools import find_packages,setup
from typing import List

dot_eee = '-e .'
requirement =[]
def get_requirement(file_path:str)->List[str]:
    with open(file_path) as file:
        requirement = file.readlines()
        requirement = [req.replace('\n','') for req in requirement]

        if dot_eee in requirement:
            requirement.remove(dot_eee)
    
        return requirement


setup(
name = 'mlproject',
version = '0.0.1',
author = 'surya',
author_email= 'sachin1702199819@gmail.com',
packages= find_packages(),
install_requires = get_requirement('requirements.text')

)