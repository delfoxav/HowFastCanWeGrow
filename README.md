# HowFastCanWeGrow

How Fast Can We Grow is a python project coming from one of my self development interrogation.

If we consider ourselves as individuals with 100 parts, with a defined probability of changing a specific number of those parts per day, how long would we take to become a completely different person? Could we even become a new person?

This project is a simulation of this process, in a sense, it is a simulation of the evolution of a person and is really similar to the concept of the Ship of Theseus or even the Moran process.

## Installation

To install the project, you can simply clone the repository and install the requirements using pip. I recommend using a virtual environment to avoid conflicts with your system's python packages.

### On Linux
```bash
git clone
cd HowFastCanWeGrow
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### On Windows
```bash
git clone
cd HowFastCanWeGrow
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Usage
The script runs a Dash web application that allows you to simulate the process of changing parts of an individual. You can change how many parts would be changed per day and what is the probability of a change happening. You can also select between considering 2 potentials outcomes or 20.

To run the application, you can simply run the following command:
```bash
python app.py
```

Then you can access the application on your browser by going to `http://localhost:8050/`.


## Comments

Of course, considering that we could only be two or twenty different people is a simplification of the problem. In reality, we could be an infinite number of different people, but this is a good way to start thinking about the problem. And to see that we can almost never change completely what we are. In a sense we are just a sum of the different person we were at different times in our lives.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contributions
Pull requests ideas on the GUI or the simulation are more than welcome. 

## Contact
If you have any questions or comments, feel free to contact me at [shonlight@gmail.com]
