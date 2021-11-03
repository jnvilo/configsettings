ConfigSettings 
==============

ConfigSettings simplifies the loading and saving of application 
configurations. Configurations can be taken from ENVIRONMENT variables
or from config files. 

ConfigSettings goal is to be an extensible application settings 
module. 

ConfigResolver classes 
-----------------------

Configuration varialbles are resolved by classes that extends apptly named  ConfigResolver.

for example:

EnvConfigResolver() : resolves configuration values from environment variables
DotFileConfigResolver() : resolves configuration values from a file 


The Configuration class
------------------------

This class loads all the ConfigResolver classes and uses them to resolve the values. 

* getInstance : returns an instance of this class 
* __getattr__(self, item):  iterates through the ConfigResolver classes to get the value of a configuration




Test
---

    make test

You can also test with a specific version of Python:

    make PYTHON_VERSION=2.7.11 test
