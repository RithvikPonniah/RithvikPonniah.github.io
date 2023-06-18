import zipfile
import pathlib

def make_Archive(filepaths,Dest_dir) :
    destPath = pathlib.Path(Dest_dir,"compressed.zip")
    with zipfile.ZipFile(destPath,'w') as archive :
        for filepath in filepaths :
            archive.write(filepath)



if __name__ == '__main__':
    make_Archive(filepaths=['day13.py','scratch.py'] , Dest_dir='dest')