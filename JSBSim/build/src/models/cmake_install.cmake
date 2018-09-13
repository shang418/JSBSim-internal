# Install script for directory: C:/Users/intern-laptop/Desktop/JSBSim/src/models

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/JSBSim/models" TYPE FILE FILES
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGAerodynamics.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGAircraft.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGAtmosphere.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGAuxiliary.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGFCS.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGSurface.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGGroundReactions.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGInertial.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGLGear.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGMassBalance.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGModel.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGOutput.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGPropagate.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGPropulsion.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGInput.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGExternalReactions.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGExternalForce.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGBuoyantForces.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGGasCell.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGAccelerations.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/FGFCSChannel.h"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("C:/Users/intern-laptop/Desktop/JSBSim/build/src/models/atmosphere/cmake_install.cmake")
  include("C:/Users/intern-laptop/Desktop/JSBSim/build/src/models/propulsion/cmake_install.cmake")
  include("C:/Users/intern-laptop/Desktop/JSBSim/build/src/models/flight_control/cmake_install.cmake")

endif()

