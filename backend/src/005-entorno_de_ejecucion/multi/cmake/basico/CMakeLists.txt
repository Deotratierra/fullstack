# Comentarios en CMake

# Requiere CMake >= v3.0
cmake_minimum_required(VERSION 3.0)

# Nombre del proyecto
project(foo)

# Creamos un ejecutable según plataforma
add_executable(foo foo.cpp)