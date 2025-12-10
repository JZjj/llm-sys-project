```python
#!/usr/bin/env python3
"""
This program defines a function to extract unique file extensions from a list of file paths.
Extensions are considered case-insensitively and returned sorted alphabetically.
Files without an extension are ignored.
"""

import os
from typing import List


def unique_file_extensions(paths: List[str]) -> List[str]:
    """
    Extract unique file extensions from file paths, case-insensitively.

    Args:
        paths: List of file path strings.

    Returns:
        Sorted list of unique file extensions (lowercase, without leading dot).
    """
    extensions = set()
    for path in paths:
        _, ext = os.path.splitext(path)
        if ext and len(ext) > 1:
            extensions.add(ext[1:].lower())
    return sorted(extensions)


def main():
    # Example usage and simple test cases
    example_paths = [
        "/home/user/document.TXT",
        "/var/log/system.log",
        "/tmp/archive.tar.gz",
        "README",
        "script.py",
        "image.JPEG",
        "archive.tar.GZ",
        "no_extension_file",
        "another.FILE.TxT"
    ]

    unique_exts = unique_file_extensions(example_paths)
    print("Unique file extensions:", unique_exts)


if __name__ == "__main__":
    main()
```