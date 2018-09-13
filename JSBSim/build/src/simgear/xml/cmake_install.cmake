# Install script for directory: C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/JSBSim/simgear/xml" TYPE FILE FILES
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/easyxml.hxx"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/ascii.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/asciitab.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/expat.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/expat_external.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/iasciitab.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/internal.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/latin1tab.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/macconfig.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/nametab.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/utf8tab.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/winconfig.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/xmlrole.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/xmltok.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/xmltok_impl.h"
    "C:/Users/intern-laptop/Desktop/JSBSim/src/simgear/xml/expat_config.h"
    )
endif()

