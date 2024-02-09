import os

# Define the project structure
project_structure = {
    "mario_game": {
        "assets": {
            "images": {},
            "sounds": {},
        },
        "levels": {},
        "src": ["main.py", "settings.py"]
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):  # It's a directory
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):  # It's a list of files
            for file_name in content:
                file_path = os.path.join(path, file_name)
                with open(file_path, 'w') as f:
                    if file_name == "main.py":
                        f.write(get_main_py_content())
                    elif file_name == "settings.py":
                        f.write(get_settings_py_content())

def get_main_py_content():
    return """import pygame
import sys

# Initialize Pygame
pygame.init()

# Here you can add your game code or import it if it's in another file

# Example game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
"""

def get_settings_py_content():
    return """# Game settings can be defined here, such as screen dimensions, paths to assets, etc.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
"""

if __name__ == "__main__":
    base_path = os.path.dirname(__file__)  # Get the directory where the script is located
    create_structure(base_path, project_structure)
