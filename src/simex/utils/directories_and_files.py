import glob
import itertools

def multiple_file_types(input_directory, *patterns, recursive=False):
    """
    Return iterable with files that have a common pattern.
    Args:
        input_directory (str): directory where files with common pattern
        will be searched.
        patterns (list): list of patterns to search for.
    Returns:
        iterable with files that have a common pattern.
    """
    return itertools.chain.from_iterable(glob.iglob(input_directory + \
                                                    "/**/*" + pattern,
                                                    recursive=recursive) for pattern in patterns)