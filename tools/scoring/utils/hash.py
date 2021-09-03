from filehash import FileHash
from dirhash import dirhash


def directory(path: str) -> tuple:
    """Generates a hash for quickly comparing directories.

    Returns:
        A tuple containing the input string and the hash/checksum as a string of hexadecimal digits
    """

    return (path, dirhash(path, "sha1", ignore=[".*", ".*/"]))


def file(path: str) -> tuple:
    """Generates a hash for quickly comparing files.

    Returns:
        A tuple containing the input string and the hash/checksum as a string of hexadecimal digits
    """

    return (path, FileHash('sha1').hash_file(path))
