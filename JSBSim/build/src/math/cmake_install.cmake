# Install script for directory: C:/Users/intern-laptop/Desktop/JSBSim/src/math

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/JSBSim/math" TYPE FILE FILES
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGColumnVector3.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGFunction.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGLocation.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGMatrix33.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGParameter.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGPropertyValue.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGQuaternion.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGRealValue.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGTable.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGCondition.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGRungeKutta.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGModelFunctions.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/LagrangeMultiplier.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGTemplateFunc.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/math/FGFunctionValue.h"
    )
endif()

