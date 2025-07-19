from setuptools import setup, find_packages

setup(
    name="iotcator_plus",
    version="0.1.0",
    packages=find_packages(where="src/python"),
    package_dir={"": "src/python"},
    install_requires=[
        # Add your dependencies here
        "angr>=9.0",
        "capstone>=4.0",
        "pyelftools>=0.28",
        # Add other required packages
    ],
    python_requires=">=3.8",
    author="Your Name",
    author_email="your.email@example.com",
    description="IoT Firmware Vulnerability Detection Framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/scott880207/Auto_Concolic",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
