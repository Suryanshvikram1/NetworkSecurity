from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    #will return list of req

    requirement_list:List[str]=[]
    try:
        with open("requirements.txt") as file:
            lines=file.readlines()

            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list


print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Suryansh Vikram Singh",
    author_email="vikramsuryanshsingh@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements() 
)