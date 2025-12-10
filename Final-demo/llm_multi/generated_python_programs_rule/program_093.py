```python
#!/usr/bin/env python3
"""
Count file extensions in a list of file paths.

The function counts file extensions case-insensitively.
Files without an extension are counted under the empty string key "".
Only the substring after the last dot is considered as the extension.
"""

from typing import List, Dict


def count_file_extensions(paths: List[str]) -> Dict[str, int]:
    """
    Count the number of files for each extension in the given list of file paths.

    Args:
        paths (List[str]): List of file path strings.

    Returns:
        Dict[str, int]: Dictionary mapping extensions (lowercase, without the dot)
                        to their counts. Files without extension map to "".
    """
    counts: Dict[str, int] = {}

    for path in paths:
        # Extract the last component after any path separator to handle paths
        # Handle both Unix and Windows separators
        filename = path.rsplit('/', 1)[-1]
        filename = filename.rsplit('\\', 1)[-1]

        # Find the last dot in the filename (if any)
        dot_index = filename.rfind('.')

        # Determine extension according to conditions:
        # - No dot or dot is first character (hidden files like ".bashrc") => no extension
        # - Dot at the end (e.g. "no_extension.") => no extension
        if dot_index <= 0 or dot_index == len(filename) - 1:
            ext = ""
        else:
            ext = filename[dot_index + 1 :].lower()

        counts[ext] = counts.get(ext, 0) + 1

    return counts


def _test() -> None:
    test_cases = [
        (
            [
                "file.txt",
                "archive.tar.gz",
                "README",
                "photo.JPG",
                "document.pdf",
                "backup.TAR.GZ",
                ".bashrc",
                "no_extension.",
                "some.dir/file.tar.gz",
                "C:\\Users\\User\\music.MP3",
                "another.file.TxT",
            ],
            {
                "txt": 2,
                "gz": 3,
                "": 3,
                "jpg": 1,
                "pdf": 1,
                "mp3": 1,
            },
        ),
    ]

    for i, (input_paths, expected) in enumerate(test_cases, 1):
        result = count_file_extensions(input_paths)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
    print("All tests passed.")


if __name__ == "__main__":
    _test()
```