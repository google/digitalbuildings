from dirhash import dirhash

def hash(dirpath: str) -> tuple:
    """Generates a hash for quickly comparing directories.

    Returns:
        A tuple containing the input string and the hash/checksum as a string of the hexadecimal digits
    """

    return (dirpath, dirhash(dirpath, "sha1", ignore=[".*", ".*/"]))
