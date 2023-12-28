import gzip


def decompress_file(filepath):
    with gzip.open(filepath, 'rb') as f:
        decompressed_data = f.read()
    return decompressed_data
