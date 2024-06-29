'''
James Truitt, digital archivist
Friends Historical Library of Swarthmore College
2024-06-05

This code is heavily indebted to several 1996 Usenet posters, especially
Ed Hamrick. See https://groups.google.com/g/rec.photo.digital/c/lkz_8p8S2U0
for the analysis on which it is based.
'''

from glob import glob

def convert_kqp_binary(binary):
    # Trim KQP garbage off front of JPEG
    magicNumber = bytes.fromhex("FF D8 FF E0") # Find beginning of JPEG
    delOffset = binary.find(magicNumber)
    binary = binary[delOffset:]

    # Create JPEG quantization table
    quantTableStr = '''
    FF DB 00 84 00 0C 08 09 0A 09 07 0C 0A 0A 0A 0E
    0D 0C 0E 12 1F 14 12 11 11 12 26 1B 1C 16 1F 2D
    27 2F 2E 2C 27 2B 2A 32 38 47 3C 32 35 43 35 2A
    2B 3E 55 3F 43 4A 4C 50 51 50 30 3C 58 5E 57 4E
    5D 47 4E 50 4D 01 0F 10 10 16 13 16 2C 18 18 2C
    5C 3D 34 3D 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C
    5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C
    5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C 5C
    5C 5C 5C 5C 5C 5C
    '''
    quantTable = bytes.fromhex(quantTableStr)

    # Insert table
    sofoEnd = bytes.fromhex('02 11 01 03 11 01')
    binary = binary.replace(sofoEnd, sofoEnd + quantTable)

    return binary


def main():
    # Get list of KQP files
    fileList = glob("*.kqp") + glob("*.KQP")
    print(f"\nFound {len(fileList)} KQP files")
    
    # Loop over files, and for each one:
    for i, file in enumerate(fileList):
        # Read the file as a bitstream
        print(f'Opening file {i+1}, {file}...', end='\t')
        with open(file, 'rb') as f:
            content = f.read()

        # Fiddle with the bitstream to make it into a valid JPG
        jpg = convert_kqp_binary(content)

        # Write the JPG to disk
        filename = file[:-4]+".jpg"
        with open(filename, 'wb') as f:
            f.write(jpg)
        print(f'Conversion done!')
    print('')

if __name__ == "__main__":
    main()