# LevitoPy


![](./images/LevitoPy.png "LevitoPy Logo")

LevitoPy is a toolbox for data analysis of Levitodynamics related experiments, including.

- Calibration (in progress)
- Simulation (in progress)
- Theory (in progress)

# installation
To use the levitopy code from anywhere (either in python or a notebook) install it via pip.

For the latest version available on GitLab

```pip install git+https://gitlab.icfo.net/pno-trappers/levitopy```

To access the example notebooks, install `levitopy` as describe above and [download](https://gitlab.icfo.net/pno-trappers/levitopy/-/tree/master/images) the notebooks.
Alternatively you can clone the entire project.

# For users

## overview
The project is structured as follows

```
levitopy
└───data                    //example data 
└───images                  //images related to levitodynamics
└───notebooks               //example notebooks
└───levitopy                //main code folder - this 
│   └───calibration         //code related to calibration of data
│   └───simulation          //code related to simulations
│   └───theory              //code related to levitodynamics theory
```

### data
Contains example data to test the code and for showcasting examples. This includes nothing yet.

### notebooks
Contains notebook examples for using the code. This includes nothing yet.

### levitopy
This folder contains the main code that makes up the `levitopy` package. If you decide to install the code this folder will be added to you `site-packages` directory.


# For developers

## Getting started

The following assumes that you know the basics. For a refresher have a look [here](https://github.com/JanGieseler/edaipynb).

If you are interested in working on the source code more directly, you can clone from our GitLab page:

```git clone https://gitlab.icfo.net/pno-trappers/levitopy```

An easy way to clone and push to the repository it to use the integrated version control of PyCharm ([howto](https://github.com/JanGieseler/edaipynb)).


## Best practice guidelines
- Follow general coding best practices, keeping in mind that the code is suppose to be read and understood by someone else.
- Add a docstring to *every* function!
- If you want to update the current package version of `levitopy` update the version number `__init__.py` file and the `comment_on_changes` string variable.
- Write test-functions whenever sensible  


