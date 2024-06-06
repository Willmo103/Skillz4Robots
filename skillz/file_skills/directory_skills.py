import json
import os
import logging
import fnmatch


logging.basicConfig(
    level=logging.DEBUG,
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    stream=None,
)
logging.getLogger().setLevel(logging.DEBUG)
_log = logging.getLogger(__name__)


class FileIgnore:
    def __init__(self):
        self._log = logging.getLogger(__name__)
        self.ignore_patterns = []
        self.except_patterns = []
        # load the ignore list from a file
        try:
            with open('ignore.json', 'r') as f:
                data = json.load(f)
            self.ignore_patterns = data.get('ignore_patterns', [])
            self.except_patterns = data.get('except_patterns', [])
            _log.info('ignore.json loaded')
        except FileNotFoundError:
            _log.info('ignore.json not found, creating a new one')
            with open('ignore.json', 'w') as f:
                json.dump({"ignore_patterns": [], "except_patterns": []}, f)
            self.ignore_patterns = []
            self.except_patterns = []
        except Exception as e:
            _log.error(f'Error loading ignore.json: {e}')
            self.ignore_patterns = []
            self.except_patterns = []

    def should_ignore(self, name):
        for pattern in self.ignore_patterns:
            if fnmatch.fnmatch(name, pattern):
                return True
        return False

    def should_except(self, name):
        for pattern in self.except_patterns:
            if fnmatch.fnmatch(name, pattern):
                return True
        return False

    def add_ignore_pattern(self, pattern):
        if pattern not in self.ignore_patterns and pattern not in self.except_patterns:
            self.ignore_patterns.append(pattern)
            self.save_ignore()

    def add_except_pattern(self, pattern):
        self.except_patterns.append(pattern)
        self.save_ignore()

    def save_ignore(self):
        with open('ignore.json', 'w') as f:
            json.dump({"ignore_patterns": self.ignore_patterns, "except_patterns": self.except_patterns}, f)
        self._log.info('ignore.json saved')

    def load_ignore(self):
        with open('ignore.json', 'r') as f:
            data = json.load(f)
        self.ignore_patterns = data.get('ignore_patterns', [])
        self.except_patterns = data.get('except_patterns', [])
        self._log.info('ignore.json loaded')
        return self.ignore_patterns, self.except_patterns


class File:
    def __init__(self, path, content, visited=False, chunk_pattern="\n\n"):
        self.path = path
        self.content = content
        self.visited = visited
        self.chunk_pattern = chunk_pattern
        self.chunks = self.split_into_chunks()

    def split_into_chunks(self):
        return self.content.split(self.chunk_pattern)


class DirectoryIngestor:
    def __init__(self, path, file_ignore):
        self.path = path
        self.structure = {}
        self.matcher = file_ignore
        self.files = []
        self.folders = []
        try:
            self.structure = self.get_structure(self.path)
        except Exception as e:
            _log.error(f'Could not initialize Codebase: {e}')
            raise Exception('Could not initialize Codebase')

    def get_structure(self, path: str):
        structure = {}
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if self.matcher.should_ignore(item):
                    continue
                if os.path.isdir(item_path):
                    subdir_ingestor = DirectoryIngestor(item_path, self.matcher)
                    if subdir_ingestor.structure:
                        structure[item] = subdir_ingestor.structure
                        self.folders.append(item_path)
                else:
                    if self.matcher.should_except(item):
                        try:
                            with open(item_path, 'r') as f:
                                content = f.read()
                                file_obj = File(path=item_path, content=content)
                                self.files.append(file_obj)
                                structure[item] = {
                                    "path": file_obj.path,
                                    "content": file_obj.content,
                                    "visited": file_obj.visited,
                                    "chunks": file_obj.chunks
                                }
                        except PermissionError as e:
                            _log.error(f'Could not read file {item_path}: {e}')
                            structure[item] = {}
                        except BlockingIOError as e:
                            _log.error(f'Could not read file {item_path}: {e}')
                            structure[item] = {}
                        except Exception as e:
                            _log.error(f'Could not read file {item_path}: {e}')
                            extension = os.path.splitext(item)[1]
                            if extension:
                                self.matcher.add_ignore_pattern(f'*{extension}')
                            structure[item] = {}
        except Exception as e:
            _log.error(f'Error traversing path {path}: {e}')
        return structure


# Example usage:
fi = FileIgnore()
codebase = DirectoryIngestor('../../../', fi)
print(json.dumps(codebase.structure, indent=4))
