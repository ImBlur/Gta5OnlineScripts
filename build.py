import PyInstaller.__main__ as pyinstaller

def build() -> None:
    pyinstaller.run(("./heist replay glitch.py", "--onefile"))
    pyinstaller.run(("./solo public session.py", "--onefile"))

if __name__ == "__main__":
    build()