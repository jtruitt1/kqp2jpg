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
    FF DB 00 84 00 07 04 05 06 05 04 07 06 05 06 07
    07 07 08 0A 11 0B 0A 09 09 0A 15 0F 10 0C 11 19
    16 1A 1A 18 16 18 18 1C 1F 28 22 1C 1D 26 1E 18
    18 23 2F 23 26 29 2A 2D 2D 2D 1B 21 31 34 31 2B
    34 28 2C 2D 2B 01 07 07 07 0A 09 0A 14 0B 0B 14
    2B 1C 18 1C 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B
    2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B
    2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B
    2B 2B 2B 2B 2B 2B
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