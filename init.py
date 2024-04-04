import os
import shutil
import subprocess


def run_commands(build_type="Debug"):
    if build_type.lower() == "release":
        settings = "build_type=Release"
    else:
        settings = "build_type=Debug"

    commands = [
        f"conan install conanfile.py --output-folder=external --build=missing --settings={settings}",
        f"cmake -S . -B build/ -DCMAKE_TOOLCHAIN_FILE=external/build/{build_type}/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE={build_type} -DCMAKE_EXPORT_COMPILE_COMMANDS=1",
    ]

    for command in commands:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)

    # check if compile_commands.json exists in the build directory, if yes, then mv and replace the old one.
    compile_commands_path = os.path.join("build", "compile_commands.json")
    if os.path.exists(compile_commands_path):
        if os.path.exists("compile_commands.json"):
            os.remove("compile_commands.json")
        shutil.move(compile_commands_path, ".")

    print("Conan install and CMake project initialization successful.")


if __name__ == "__main__":
    while True:
        user_input = input(
            'Type "release" to initialize in Release Mode, or press Enter to continue in Debug Mode...'
        )

        if user_input.lower() == "release" or user_input.strip() == "":
            break

    BUILD_TYPE_ARG = "Release" if user_input.lower() == "release" else "Debug"

    if not os.path.exists("build/"):
        os.makedirs("build/")
    run_commands(BUILD_TYPE_ARG)
