cmake_minimum_required(VERSION 2.6)
project(Pendbot)

set(sdir ${CMAKE_CURRENT_SOURCE_DIR})
set(idir ${CMAKE_CURRENT_SOURCE_DIR}/include)
set(sdir ${CMAKE_CURRENT_SOURCE_DIR}/src)

file(GLOB SOURCES ${sdir}/*.cpp)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS ${CMKAE_CXX_FLAS} "-std=c++11")


add_executable(Pbot ${SOURCES})
target_include_directories(Pbot PRIVATE BEFORE ${idir})






