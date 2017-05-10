# CMake下指定Opencv版本

关键文件：OpenCVConfig.cmake。在opencv编译好后，所在目录中一般会有一个叫OpenCVConfig.cmake的文件，这个文件中指定了CMake要去哪里找OpenCV，其.h文件在哪里等，比如其中一行：

		# Provide the include directories to the caller
		set(OpenCV_INCLUDE_DIRS "/home/ubuntu/src/opencv-3.1.0/build" "/home/ubuntu/src/opencv-3.1.0/include" "/home/ubuntu/src/opencv-3.1.0/include/opencv")

只要让CMake找到这个文件，这个文件就指定了Opencv的所有路径，因此设置OpenCV_DIR为包含OpenCVConfig.cmake的目录，如在我的C++工程CMakeLists.txt中添加

	set(OpenCV_DIR "/home/ubuntu/src/opencv-3.1.0/build")

我的OpenCVConfig.cmake在

	/home/ubuntu/src/opencv-3.1.0/build

注意，将其添加在project(MyProjectName)之前。

如CMakeLists.txt内容如下：

	cmake_minimum_required(VERSION 2.8)
	set(OpenCV_DIR "/home/ubuntu/src/opencv-3.1.0/build")
	project( camera )
	find_package( OpenCV REQUIRED )
	add_executable( camera camera.cpp )
	target_link_libraries( camera ${OpenCV_LIBS} )

因此，我们期望使用哪个版本的Opencv，只要找到对应的OpenCVConfig.cmake文件，并且将其路径添加到工程的CMakeLists.txt中即可了。
