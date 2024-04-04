from conan import ConanFile
from conan.tools.cmake import cmake_layout


class ProjectRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("spdlog/1.13.0")
        self.requires("boost/1.84.0")

    def layout(self):
        cmake_layout(self)
