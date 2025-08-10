from setuptools import setup,find_packages
from typing import List
HYPRN_E_DOT="e ."
def get_requrements(file_path:str)->List[str]:
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if HYPRN_E_DOT in requirements:
            requirements.remove(HYPRN_E_DOT)
    return
setup(
    name='mlproject',
    version='0.0.1',
    author='Ravula ponnakrishnavamsi',
    author_email="ponnakrishnavamsi@gmail.com",
    install_requirements=get_requrements('requirement.txt')

)