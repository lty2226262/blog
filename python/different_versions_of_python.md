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
