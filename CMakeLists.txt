cmake_minimum_required(VERSION 3.18)
project(ExpressionSolver)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake")
include(ucm)
include_directories("${PROJECT_SOURCE_DIR}/libs/cosmopolitan")

#vanilla flags
ucm_add_flags(CXX "-std=c++${CMAKE_CXX_STANDARD}")

#warnings
ucm_add_flags(CXX
        -Wall -Wextra
        -fmax-errors=5
        -Wno-c99-designator -Wno-unused-command-line-argument
        -Wno-deprecated-enum-enum-conversion -Wno-deprecated-anon-enum-enum-conversion
        -Wno-c++20-compat -Wno-c++98-compat -Wno-pre-c++17-compat -Wno-c++98-compat-pedantic
        -Wno-padded -Wno-gnu-anonymous-struct -Wno-nested-anon-types
        -Wno-missing-noreturn -Wno-float-equal -Wno-implicit-int-float-conversion
        -Wno-sign-conversion -Wno-ctad-maybe-unsupported -Wno-class-varargs
        -Wno-old-style-cast -Wno-shadow -Wno-reserved-macro-identifier
)

# Debug flags
ucm_add_flags(CXX -ggdb3 -fno-eliminate-unused-debug-types)

#required flags to build project
ucm_add_flags(CXX 
    -static 
    -march=x86-64)

# Add an executable with the above sources
add_executable(${PROJECT_NAME}
    src/main.cpp
)

target_link_libraries(${PROJECT_NAME})
