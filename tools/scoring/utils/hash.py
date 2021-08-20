from dirhash import dirhash

def hash(dirpath: str) -> tuple:
    return (dirpath, dirhash(dirpath, "sha1", ignore=[".*", ".*/"]))
