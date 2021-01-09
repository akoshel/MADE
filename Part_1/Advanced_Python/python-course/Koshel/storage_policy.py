import struct
class StoragePolicy:
    @staticmethod
    def dump(word_to_docs_mapping, filepath: str):
        fout = open(filepath, 'wb')
        fout.write(struct.pack('i', len(word_to_docs_mapping)))
        for key, value in word_to_docs_mapping.items():
            key_len = len(key)
            fout.write(struct.pack('B', len(key)))
            fout.write(struct.pack(f'{key_len}s', key.encode('utf-8')))
            val_len = len(value)
            fout.write(struct.pack('h', val_len))
            for v in value:
                fout.write(struct.pack('h', v))
        fout.close()


    @staticmethod
    def load(filepath: str):
        unpacked_dict = {}
        with open(filepath, mode='rb') as file:  # b is important -> binary
            file_content = file.read()
        dict_size = struct.unpack('i', file_content[: 4])[0]
        start_index = 4
        for _ in range(dict_size):
            key_len = file_content[start_index]
            try:
                key = struct.unpack(f'{key_len}s',
                                    file_content[start_index + 1: start_index + key_len + 1])[0].decode("utf-8")
            except UnicodeDecodeError:
                key = struct.unpack(f'{key_len}s',
                                    file_content[start_index + 1: start_index + key_len + 1])[0]
            val_len = struct.unpack('h', file_content[start_index + key_len + 1: start_index + key_len + 3])
            unpacked_dict[key] = list(struct.unpack(
                f'{val_len[0]}h', file_content[start_index + key_len + 3: start_index + key_len + 3 + val_len[0] * 2]))
            start_index = start_index + key_len + 3 + val_len[0] * 2
        file.close()
        return unpacked_dict
