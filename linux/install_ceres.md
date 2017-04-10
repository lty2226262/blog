git clone https://github.com/ceres-solver/ceres-solver

sudo apt-get install liblapack-dev libsuitesparse-dev libcxsparse3.1.2 libgflags-dev libgoogle-glog-dev libgtest-dev

cmake ..
make -j8
make -j8 install
