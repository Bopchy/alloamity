# AlloAmity - Office Space Allocation System

Alloamity is a command line office space allocation system for one of Andela's facilities known as Amity. Amity has both Offices and Livng spaces. Offices can hold a maximum of six people, whereas living spaces can hold a maximum of four people. Both fellows and staff members require an office space, while only fellows can be allocated a living space. Alloamity allocates staff members and fellows to rooms randomly.  

## Installation

Clone `https://github.com/Bopchy/checkpoint-1.git`

## Virtual Environment and Dependencies 

Create a python 3 virtual environment by running:
	
	virtualenv --python=python3 cp-venv

Activate the just created environment by running: 
	
	source cp-venv/bin/activate

Then install the necessary dependencies by navigating to the root folder of the project and running 
	
	pip install -r requirements.txt

## Tests

To run tests run:

	nosetests

## To run the application:

	python amity_docopt.py

