# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from hashlib import sha256

def calculate_hash(text: str) -> str:
    """
    Calculate SHA256 hash of the input text

    Returns
    -------
    str
    """
    sha256_hash = sha256()

    chunk_size = 4096

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        sha256_hash.update(chunk.encode('utf-8'))

    return sha256_hash.hexdigest()