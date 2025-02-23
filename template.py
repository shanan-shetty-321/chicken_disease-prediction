#for putting path and creating new folders and all so that we dont need to code to add new folder again
#
import os
import logging #whenever template.py will run it will prepare some logs
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
#initialize logging level to information level
#it prints log in terminal , as it is an info log , it will show timestamp with logging message
#we will store logs
project_name="chickendisease"
list_of_files=[   #all files and folder needed in project can be defined here
    ".github/workflows/.gitkeep",
#for deployment when we use ci/cd deployment and create a .eml file in future .gitkeep file if u
    # commit any empty folder it would show in github
    #remove gitkeep file in future after creating .eml file
    f"src{project_name}/__init__.py",
    #we r creating a source file which will keep all the contents that are needed
    #for building and running the project , we need that constructor file seperate for each local package folder 
    #(constructor file is used to initialize objects in oop, so in large projects  where
    # initialization logic (such as setting default values, loading resources, or connecting to a database) needs to be structured separately.
    #constructor logic is often moved to a separate file to improve code organization, reusability, and maintainability. Instead of writing initialization code inside each class or module,
    # we create a separate file that handles object setup and dependencies.
    f"src{project_name}/components/__init__.py",
    #constructor file seperate for each local package folder (components)
    #this file will contain modular(breaking code into reusable components which handles a specific functionality)
    # , reusable pieces of code to handle specific feature
    #all these functionalities are core functionalities or independent modules of project handling some business logic or a specific feature 
    # component files ke Purpose: Defines reusable parts (or "components") of a larger system.
# 🔹 Common Use Cases:
# 
# A module for handling database operations.
# A component for processing images in an ML pipeline.
# A class/module responsible for user authentication.
    #
    f"src{project_name}/utils/__init__.py",
    #A utils.py (utilities file) is a helper module that contains reusable functions, classes, or configurations used across multiple parts of a project.
    # Instead of repeating the same logic in multiple files,
    # we keep them in utils.py for better code organization and reusability.A utils (utility) file contains helper functions used across different components to avoid duplication.
    # 🔹 Purpose: Provides generic, reusable functions that multiple components can call.
    # 🔹 Common Use Cases:
    # 
    # Functions for reading/writing files.
    # Data normalization and transformation functions.
    # Generic functions like logging, API requests, and calculations.
    
    
    
    f"src{project_name}/config/__init__.py",
#     Definition: A config file contains configuration settings, such as API keys, database credentials, file paths, model hyperparameters, etc.
# 🔹 Purpose: Centralizes all environment-dependent or changeable settings.
# 🔹 Common Use Cases:
# 
# Storing file paths, API keys, database settings.
# Defining model hyperparameters in an ML project like learnong rate,etc.
#  Setting global constants used across the project.
#has key value pair / constants
    f"src{project_name}/config/configuration.py",
    f"src{project_name}/pipeline/__init__.py",
    f"src{project_name}/entity/__init__.py",
    f"src{project_name}/constants/__init__.py",
    "config/config.yaml",#config folder mein config file of type yaml
    "dvc.yaml" , #mlops tool
    "params.yaml",# for parameters
    "requirements.txt",#it will have all the requirement package of code
    "setup.py",
    "research/trial.ipynb",#doing some notebook experiment
    "templates/index.html"
]



for filepath in list_of_files:  #looping through list which follows
    filepath=Path(filepath)
#we have given forward slash for our project address but windows use backward slash
# instead of forwad slash, forward slash is used in linux os. Path(filepath)
# converts it to windows path
    filedir,filename=os.path.split(filepath)
    #here we r getting 2 things in return from os.path- folder and file as a tuple
    if(filedir != ""): #if the directory name (a folder with no files)
        os.makedirs(filedir,exist_ok=True)
        #make the directory and make the file , so this file wont be creted again if run again due to
        #exist_ok=true

        #logg the info
        logging.info(f"creating directory ; {filedir} for the file :{filename}")
    if( not os.path.exists(filepath)  or os.path.getsize(filepath)==0):
        #dono mein se any  condition can be used for saying if the directory doesnt exist
        #then create the file
        with open(filepath,"w")  as f:   #i will create that file with write mode
            pass
            logging.info(f"creating empty file : {filepath}")

    else: #if file already exists
        logging.info(f"{filename} already exists")

