# kqp2jpg
Small, rough Python script to convert KQP files to JPG.

This script is heavily indebted to several 1996 Usenet posters, especially
Ed Hamrick. See https://groups.google.com/g/rec.photo.digital/c/lkz_8p8S2U0
for the analysis on which it is based.

## Background
> .KQP is a raster graphics format associated with Konica Picture Show, and related software (PC PictureShow).

— [justsolve.archiveteam.org](http://justsolve.archiveteam.org/wiki/KQP)

> Just before the turn of the century, Konica partnered with photo shops and drugstores to run a scanning service for home photos. After developing your pictures, they would scan your film for a small fee ... and give you a floppy disk with digital photos and a copy of the Konica “PC PictureShow” program. The program automatically loads the images on the disk and lets you view photos on your PC. The scans are only 600 x 400 pixels, but that was plenty large for your average home snapshots back in 1999.

— [Parts Not Included](https://www.partsnotincluded.com/converting-konica-quality-photo-kqp-files/)

Unfortunately, this is a proprietary file format. The creator, Konica, "merged with Minolta to form Konica Minolta in 2003, and ... then got out of the camera business in 2006 – selling most of its operations to Sony" ([Parts Not Included](https://www.partsnotincluded.com/converting-konica-quality-photo-kqp-files/)). Despite that, however, the format is more or less a modified JPEG, which has allowed conversion into that format.

## Usage

Navigate to the folder containing the KQP files you wish to convert, then invoke the Python script.

