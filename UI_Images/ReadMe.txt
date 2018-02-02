I want to put limelight over this project titled "No-Escape Search", it is a exhaustive cloud based in-file content search, aims to retrieve user requested string's location in O(constant)time usually 3-5 seconds.

It's involves:
1) Frontend implemented with PyQt. As user inputs a word. Our algorithm searches every word (crores of words) inside every file (hundreds of file) to display closest result within 3-5 seconds.
2) Automated directory scanner that automatically starts scanning a directory and creates a 3D hash table over cloud whenever a file is inserted in particular directory.