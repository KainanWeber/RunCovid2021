import cx_Freeze
executables = [cx_Freeze.Executable(
    script="jogo.py", icon="assets/passanóisMarcao.ico")]

cx_Freeze.setup(
    name="Run From Covid",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]
                           }},
    executables=executables
)
