import unittest
import tempfile
import os
import shutil
from skillz.file_skills.directory_skills import FileIgnore, File, DirectoryIngestor, Directory


class TestFileIgnore(unittest.TestCase):
    def setUp(self):
        self.file_ignore = FileIgnore()

    def test_ignore_patterns(self):
        self.file_ignore.add_ignore_pattern("*.tmp")
        self.assertIn("*.tmp", self.file_ignore.ignore_patterns)

    def test_except_patterns(self):
        self.file_ignore.add_except_pattern("*.txt")
        self.assertIn("*.txt", self.file_ignore.except_patterns)

    def test_should_ignore(self):
        self.file_ignore.add_ignore_pattern("*.tmp")
        self.assertTrue(self.file_ignore.should_ignore("file.tmp"))

    def test_should_except(self):
        self.file_ignore.add_except_pattern("*.txt")
        self.assertTrue(self.file_ignore.should_except("file.txt"))


class TestFile(unittest.TestCase):
    def test_split_into_chunks(self):
        content = "Chunk1\n\nChunk2\n\nChunk3"
        file = File(path="dummy.txt", content=content)
        self.assertEqual(file.chunks, ["Chunk1", "Chunk2", "Chunk3"])


class TestDirectoryIngestor(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.file_ignore = FileIgnore()
        self.create_test_files_and_folders()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def create_test_files_and_folders(self):
        os.makedirs(os.path.join(self.test_dir, "folder1"), exist_ok=True)
        os.makedirs(os.path.join(self.test_dir, "folder2"), exist_ok=True)

        with open(os.path.join(self.test_dir, "file1.txt"), 'w') as f:
            f.write("Content of file1")
        with open(os.path.join(self.test_dir, "file2.txt"), 'w') as f:
            f.write("Content of file2")

    def test_get_structure(self):
        di = DirectoryIngestor(self.test_dir, self.file_ignore)
        self.assertIn("file1.txt", di.structure)
        self.assertIn("folder1", di.structure)


class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.file_ignore = FileIgnore()
        self.create_test_files_and_folders()
        self.directory = Directory(self.test_dir, self.file_ignore)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def create_test_files_and_folders(self):
        os.makedirs(os.path.join(self.test_dir, "folder1"), exist_ok=True)
        os.makedirs(os.path.join(self.test_dir, "folder2"), exist_ok=True)

        with open(os.path.join(self.test_dir, "file1.txt"), 'w') as f:
            f.write("Content of file1")
        with open(os.path.join(self.test_dir, "file2.txt"), 'w') as f:
            f.write("Content of file2")

    def test_get_next_file(self):
        file = self.directory.get_next_file()
        self.assertIsNotNone(file)
        self.assertEqual(file.path, os.path.join(self.test_dir, "file1.txt"))
        self.assertTrue(file.visited)

        file = self.directory.get_next_file()
        self.assertIsNotNone(file)
        self.assertEqual(file.path, os.path.join(self.test_dir, "file2.txt"))
        self.assertTrue(file.visited)

        file = self.directory.get_next_file()
        self.assertIsNone(file)

    def test_get_next_folder(self):
        folder = self.directory.get_next_folder()
        self.assertIsNotNone(folder)
        self.assertTrue(folder.endswith("folder1"))

        folder = self.directory.get_next_folder()
        self.assertIsNotNone(folder)
        self.assertTrue(folder.endswith("folder2"))

        folder = self.directory.get_next_folder()
        self.assertIsNone(folder)


if __name__ == '__main__':
    unittest.main()
