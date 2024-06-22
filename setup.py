from setuptools import setup, find_packages

setup(
    name='theetl',
    version='0.1.0',
    author='Ismael Sanchez',
    author_email='isanchezcasado@gmail.com',
    description='Custom ETL library for Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='git@github.com:ismaello/theetl.git',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'importlib' 
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: GNU License',
        'Operating System :: OS Independent',
    ],
)
