CMake:

		cmake .. -G Ninja
		ninja
		ninja test
		sudo ninja install

Catkin_make:

		catkin_make_isolated --install --use-ninja
		source install_isolated/setup.bash
