import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

requires = [
    "numpy>=1.14.5"
]

packages = [
    "quantum_computer_simulator"
]

setuptools.setup(
    name="quantum-computer-simulator",
    version="0.0.1",
    author="Alistair O'Brien",
    author_email="alistair@duneroot.co.uk",
    description="A Quantum Computer Simulator written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnyob/Quantum-Computer-Simulator",
    packages=packages,
    install_requires=requires
)
