import pathlib
import shutil

# shutil.make_archive('lesson6', 'zip')

path = pathlib.Path(r'D:\GitRepository\GoIT-work\01_CORE\12\01 Lessons\06.1\archive')
# path.mkdir()

# shutil.make_archive('lesson6', 'zip')

# with open('lesson6.zip', 'rb',) as fd:
#     print(len(fd.read()))

shutil.unpack_archive('Python12.zip', path)