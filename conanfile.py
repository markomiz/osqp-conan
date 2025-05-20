from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import copy
import os

class OsqpConan(ConanFile):
    name = "osqp"
    version = "1.0.0"
    license = "Apache-2.0"
    author = "Oscar Axhede, Bartolomeo Stellato"
    url = "https://github.com/markomizdrak/osqp"
    description = "The Operator Splitting QP Solver"
    topics = ("quadratic-programming", "optimization", "math", "qp")
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    exports_sources = [
        "CMakeLists.txt",
        "src/*",
        "include/*",
        "lin_sys/*",
        "external/*",
        "algebra/*",
        "configure/*",
        "cmake/*",
        "Utils/*",
        "codegen/*",
        "examples/*",
        "tests/*",
        "LICENCE"
    ]
    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        # Headers
        copy(self, pattern="*.h", dst=os.path.join(self.package_folder, "include"), src="include", keep_path=True)
        copy(self, pattern="*.hpp", dst=os.path.join(self.package_folder, "include"), src="include", keep_path=True)
        copy(self, pattern="*.tpp", dst=os.path.join(self.package_folder, "include"), src="include", keep_path=True)

        # (Optional, if you also expect files in the build dir)
        copy(self, pattern="*.h", dst=os.path.join(self.package_folder, "include"), src=os.path.join(self.build_folder, "include"), keep_path=True)
        copy(self, pattern="*.hpp", dst=os.path.join(self.package_folder, "include"), src=os.path.join(self.build_folder, "include"), keep_path=True)
        copy(self, pattern="*.tpp", dst=os.path.join(self.package_folder, "include"), src=os.path.join(self.build_folder, "include"), keep_path=True)


        # Static and shared libraries
        copy(self, "*.a", dst="lib", src=self.build_folder, keep_path=False)
        copy(self, "*.so*", dst="lib", src=self.build_folder, keep_path=False)
        copy(self, "*.dylib*", dst="lib", src=self.build_folder, keep_path=False)
        copy(self, "*.dll*", dst="bin", src=self.build_folder, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["osqp"]
