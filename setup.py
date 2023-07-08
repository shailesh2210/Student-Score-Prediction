from setup.tools import setup, find_packages
from typing import List

HYPEN_DOT_E = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", " ")for req in requirements.txt]


        if HYPEN_DOT_E in requirements:
                requirements.remove(HYPEN_DOT_E)

    return requirements

setup(
    name = "Practice Ml Project",
    version = "0.0.1",
    author = "Shailesh Gaddam"
    author_email = "shaileshgaddam22@gmail.com"
    find_packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)

