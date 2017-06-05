# Virutalenv

sudo pip install virtualenv

virtualenv envname  ##创建一个新的隔离环境  

激活虚拟环境

source ENV/bin/activate

离开虚拟环境

deactive

# Pyenv

## Install different versions of python

		python install <version>
		pyenv install 3.3.0

</br>

		pyenv local 3.3.0 #将当前目录下的Python环境切换为3.3.0

		pyenv virtualenv 3.3.0 env 创建一个Python版本为3.3.0 的环境，环境叫做env
		pyenv activate env #激活env这个环境
		pyenv deactivate #离开已经激活的环境


# Most useful -- anaconda

With Anaconda, it's simple to install the packages you'll often use in data science work. You'll also use it to create virtual environments that make working on multiple projects much less mind-twisting.

## Managing packages

conda is not Python specific like pip is, it can also install non-Python packages.

## Environment

It's similar to virtualenv and pyenv, other popular environment managers.

## Installing Anaconda

https://www.continuum.io/downloads#macos

export PATH="/Users/zc/anaconda/bin:$PATH"

## Managing Packages

		conda install numpy=1.10

		conda update --all

## Managing environments

		conda create -n env_name list of packages

Here -n env_name sets the name of your environment (-n for name) and list of packages is the list of packages you want installed in the environment. For example, to create an environment named my_env and install numpy in it, type:
		
		conda create -n my_env numpy
		conda create -n py3 python=3

## Entering an environment

Once you have an environment created, use source activate my_env to enter it on OSX/Linux.

## Saving and loading environments

You can save the packages to a YAML file with 

		conda env export > environment.yaml. 

The first part: 

		conda env export 

writes out all the packages in the environment, including the Python version.

The second part of the export command, 

		> environment.yaml 

writes the exported text to a YAML file environment.yaml.

To create an environment from an environment file use 

conda env create -f environment.yaml

This will create a new environment with the same name listed in environment.yaml.

## Listing environments

 		conda env list 

 to list out all the environments you've created

## Removing environments

If there are environments you don't use anymore,

		conda env remove -n env_name 

will remove the specified environment (here, named env_name).