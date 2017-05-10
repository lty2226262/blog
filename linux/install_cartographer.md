sudo apt-get install -y google-mock libboost-all-dev libeigen3-dev libgflags-dev libgoogle-glog-dev liblua5.2-dev libprotobuf-dev libsuitesparse-dev libwebp-dev ninja-build protobuf-compiler python-sphinx ros-kinetic-tf2-eigen libatlas-base-dev libsuitesparse-dev liblapack-dev

		git clone https://github.com/hitcm/ceres-solver-1.11.0.git // ceres path
		cd ceres-solver-1.11.0/build
		cmake ..
		make –j
		sudo make install

</br>

		git clone https://github.com/hitcm/cartographer.git
		cd cartographer/build
		cmake .. -G Ninja
		ninja
		ninja test
		sudo ninja install

</br>

		git clone https://github.com/hitcm/cartographer_ros.git
