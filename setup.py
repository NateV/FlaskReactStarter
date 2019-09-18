from setuptools import setup

setup(
    name="Flask React Starter app",
    packages=[  
        "server",
    ],
    include_package_data=True,
    install_requires=[
        "flask",
    ],
)