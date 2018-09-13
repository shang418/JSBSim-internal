# Install script for directory: C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/JSBSim/models/flight_control" TYPE FILE FILES
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGDeadBand.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGFCSComponent.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGFilter.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGGain.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGKinemat.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGSummer.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGSwitch.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGFCSFunction.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGSensor.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGPID.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGActuator.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGAccelerometer.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGGyro.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGMagnetometer.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGSensorOrientation.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGAngles.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGWaypoint.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/models/flight_control/FGDistributor.h"
    )
endif()

