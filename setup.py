from setuptools import setup ,find_packages
from typing import List

def get_requirements(file_path:str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements



setup(

name = "new_project",
version = '0.0.1',
author='hira mariam',
author_email='hiramariam@neduet.edu.pk',
packages=find_packages(),
install_requirements = get_requirements('requirements.txt')

)