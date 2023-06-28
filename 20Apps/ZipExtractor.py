import zipfile

def ExtractArchive(archivePath, Dest_Dir):
    with zipfile.ZipFile(archivePath,'r') as archive :
        archive.extractall(Dest_Dir)


if __name__ == "__main__" :
    ExtractArchive("/Users/rajap/Documents/GitHub/RithvikPonniah.github.io/20Apps/compressed (1).zip",
                   "/Users/rajap/Documents/GitHub/RithvikPonniah.github.io/20Apps/files")