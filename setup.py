# this file is created to manage packaging the ML project
from setuptools import find_packages,setup
from typing import List

def get_requires(file_path:str):
    '''
    this function return the list of requierments
    '''
    HYPHEN_E_DOT = '-e .' # it connects the requirements.txt to setup file
    requiermnets = []
    with open(file_path) as file_obj:
        requiermnets = file_obj.readlines()
        requiermnets=[req.replace("\n",'') for req in requiermnets]
        if HYPHEN_E_DOT in requiermnets:
            requiermnets.remove(HYPHEN_E_DOT)
    return requiermnets
 
setup(
    name='mlproject',
    version='0.0.1',
    author='sara',
    author_email='sarasaberi.mt@gmail.com',
    packages=find_packages(),
    # install_requires= ['pandas','numpy','seaborn']
    install_requires = get_requires('./requierments.txt')

)