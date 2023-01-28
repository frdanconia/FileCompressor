import os
import zlib

class FileCompressor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.compressed_file_path = self.file_path + '.gz'
        
    def compress(self, level=6):
        """
        Compresses the file specified in the constructor using zlib
        :param level: Compression level (1-9)
        """
        with open(self.file_path, 'rb') as f_in:
            data = f_in.read()
            compressed_data = zlib.compress(data, level)

            with open(self.compressed_file_path, 'wb') as f_out:
                f_out.write(compressed_data)
                
        print(f"Successfully compressed {self.file_path} to {self.compressed_file_path}")

    def decompress(self):
        """
        Decompresses the compressed file
        """
        with open(self.compressed_file_path, 'rb') as f_in:
            compressed_data = f_in.read()
            decompressed_data = zlib.decompress(compressed_data)

            with open(self.file_path, 'wb') as f_out:
                f_out.write(decompressed_data)

    def compress_multiple_files(self, file_paths, level=6):
        """
        Compresses multiple files using zlib
        :param file_paths: List of file paths to compress
        :param level: Compression level (1-9)
        """
        for file_path in file_paths:
            compressor = FileCompressor(file_path)
            compressor.compress(level)
                
        print(f"Successfully decompressed {self.compressed_file_path} to {self.file_path}")
        
    def compress_and_decompress(self):
        """
        Compresses and then decompresses the file
        """
        self.compress()
        self.decompress()
        
    def remove_compressed_file(self):
        """
        Removes the compressed file
        """
        os.remove(self.compressed_file_path)
        print(f"Successfully removed {self.compressed_file_path}")

     def get_file_sizes(self):
        """
        Returns the original size and compressed size of the file
        """
        original_size = os.path.getsize(self.file_path)
        compressed_size = os.path.getsize(self.compressed_file_path)
        return original_size, compressed_size

compressor = FileCompressor('test.txt')
compressor.compress()
compressor.decompress()
compressor.remove_compressed_file()