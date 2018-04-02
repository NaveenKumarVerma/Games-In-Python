import cx_Freeze

executables = [cx_Freeze.Executable("PlayGame.py")]

cx_Freeze.setup(
    name="Game Box",
    options={
              "build_exe":{"packages":["pygame"], 
	     "include_files":["snakehead.png",
			      "apple.png",
                              "lost.jpg",
                              "tan.jpg",
                              "win.jpg",
                              "beep.wav",
                              "bomb.ogg",
                              "hit.wav",
                              "slither.py",
                              "Tanks.py",
			      "slither.pyc",
			      "Tanks.py"]}},

    description = "Game Box",
    executables = executables
    )
