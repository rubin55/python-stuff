# A collection of various things in Python

This is my Python experiments and other things repository. You'll find various directories with Python source code in them and invariably a `requirements.txt` file. You can work with the code in the relevant subdirectory by creating a Python virtual environment and installing the requirements:

    python -m venv venv
    . venv/bin/activate
    pip install -r ./ccspp/requirements.txt -r ./jupyter/requirements.txt -r ./rabbit/requirements.txt -r ./tensor/requirements.txt
    python something.py

Note: you don't *have* to install all requirements in a single `venv`. Currently there are no conflicts between the various requirements. If that ever changes you might opt to only install the requirements you specifically need for what you're working on at that moment.
