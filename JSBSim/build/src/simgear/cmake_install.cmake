# Install script for directory: C:/Users/intern-laptop/Desktop/JSBSim/src/simgear

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Program Files (x86)/JSBSim")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevelx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/JSBSim/simgear" TYPE FILE FILES "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/compiler.h")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("C:/Users/intern-laptop/Desktop/JSBSim/build/src/simgear/structure/cmake_install.cmake")
  include("C:/Users/intern-laptop/Desktop/JSBSim/build/src/simgear/props/cmake_install.cmake")
  include("C:/Users/intern-laptop/Desktop/JSBSim/build/src/simgear/magvar/cmake_install.cmake")
  include("C:/Users/intern-laptop/Desktop/JSBSim/build/src/simgear/misc/cmake_install.cmake")
  include("C:/Users/intern-laptop/Desktop/JSBSim/build/src/simgear/xml/cmake_install.cmake")
  include("C:/Users/intern-laptop/Desktop/JSBSim/build/src/simgear/io/iostreams/cmake_install.cmake")

endif()

