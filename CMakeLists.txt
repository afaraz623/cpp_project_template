cmake_minimum_required(VERSION 3.15)

project(logging LANGUAGES CXX)

set(CMAKE_CXX_COMPILER "clang++")

find_package(spdlog REQUIRED)
find_package(Boost REQUIRED COMPONENTS asio)

add_executable(${PROJECT_NAME} src/main.cpp)
target_link_libraries(${PROJECT_NAME} spdlog::spdlog Boost::boost)
