1. **Huffman Coding**:
    - A lossless data compression algorithm using variable-length codes.
    - More frequent symbols get shorter codes.
2. **Lempel-Ziv-Welch (LZW)**:
    - Dictionary-based compression.
    - Suitable for repetitive sequences. Used in GIFs.
3. **LZ77 and LZSS**:
    - Finds repeated sequences in a "sliding window".
    - Used in `gzip`, `zlib`, etc.
4. **LZMA**:
    - High compression ratios but computationally intensive.
    - Used in 7-Zip.
5. **Run-Length Encoding (RLE)**:
    - Good for long sequences of repeated bits.
6. **Burrows-Wheeler Transform (BWT)**:
    - Places similar data nearby. Used in `bzip2`.
7. **Arithmetic Coding**:
    - Represents sequences as an interval between 0 and 1.
8. **Delta Encoding**:
    - Stores differences between sequential data.
9. **Shannon-Fano Coding**:
    - An older method, precursor to Huffman coding.