import shutil
import subprocess


def blender_animation_engine(blender_file, script_file):

    blender_exe = shutil.which("blender")
    if blender_exe:
        print(f"Found: {blender_exe}")
    else:
        print("Unable to find Blender!")
        return
    subprocess.call([blender_exe, '-b', blender_file, '-P', script_file])
