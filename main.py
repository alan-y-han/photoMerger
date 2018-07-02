import os

folderPath = "C:/path/to/photos/"

folders = [folderPath + folderName + "/" for folderName in os.listdir(folderPath) if not os.path.isfile(folderName)]
count = 1
timeOffset = 0 # add an optional offset to all nPhoto timestamps

for folder in folders:
    print(folder)

    nPath = folder
    iPath = folder + "iPhone/"

    nPhotos = [(nFile, os.path.getmtime(nPath + nFile) + timeOffset, True)
               for nFile in os.listdir(nPath)
               if os.path.isfile(nPath + nFile)]
    iPhotos = [(iFile, os.path.getmtime(iPath + iFile), False)
               for iFile in os.listdir(iPath)
               if os.path.isfile(iPath + iFile)]

    sortedPhotos = []

    while len(nPhotos) and len(iPhotos):
        _, nTime, _ = nPhotos[0]
        _, iTime, _ = iPhotos[0]

        if nTime < iTime:
            sortedPhotos.append(nPhotos.pop(0))
        else:
            sortedPhotos.append(iPhotos.pop(0))

    if len(nPhotos):
        sortedPhotos.extend(nPhotos)
    elif len(iPhotos):
        sortedPhotos.extend(iPhotos)

    for file in sortedPhotos:
        fileName, modTime, isNPhoto = file
        _, fileExtension = os.path.splitext(fileName)

        newName = ""
        if isNPhoto:
            newName = str(count).zfill(3) + "_n" + fileExtension
            print(nPath + fileName)
            print(nPath + newName)
            os.rename(nPath + fileName, nPath + newName)
        else:
            newName = str(count).zfill(3) + "_i" + fileExtension
            print(iPath + fileName)
            print(nPath + newName)
            os.rename(iPath + fileName, nPath + newName)

        print("")

        count += 1
