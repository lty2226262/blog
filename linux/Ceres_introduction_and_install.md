Ceres Solver is an open source C++ library for modeling and solving large, complicated optimization problems. It can be used to solve Non-linear Least Squares problems with bounds constraints and unconstrained problems.

sudo apt-get install liblapack-dev libsuitesparse-dev libcxsparse3.1.4 libgflags-dev libgoogle-glog-dev libgtest-dev

git clone https://github.com/ceres-solver/ceres-solver

mkdir build && cd build

cmake ..

make -j8

make -j8 install