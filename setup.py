from setuptools import find_packages,setup
from typing import List
hyphen_e = '-e .'

def get_requirements(file_path:str)-> List[str]:
    requirement =[]

    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement = [req.replace("\n","") for req in requirement]

        if hyphen_e in requirement:
            requirement.remove(hyphen_e)

    return requirement



setup(
    name="MLprojects",
    version='0.0.1',
    author="rishvy",
    author_email='rishvykttk@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)