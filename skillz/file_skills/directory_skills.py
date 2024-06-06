import json
import os
import logging
import fnmatch

logging.basicConfig(level=logging.DEBUG)
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
        if pattern not in self.ignore_patterns or pattern:
            self.ignore_patterns.append(pattern)
            self.save_ignore()

    def add_except_pattern(self, pattern):
        if pattern not in self.except_patterns:
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


class DirectoryIngestor:
    def __init__(self, path):
        self.path = path
        self.structure = {}
        self.matcher = FileIgnore()
        try:
            self.structure = self.get_structure(self.path)
        except Exception as e:
            _log.error(f'Could not initialize Codebase: {e}')
            raise Exception('Could not initialize Codebase')
        self.files = []
        self.folders = []

    def get_structure(self, path: str):
        structure = {}
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if self.matcher.should_ignore(item):
                    continue
                if os.path.isdir(item_path):
                    subdir = self.get_structure(item_path)
                    if subdir:
                        structure[item] = subdir
                        self.folders.append(item_path)
                else:
                    if self.matcher.should_except(item):
                        try:
                            with open(item_path, 'r') as f:
                                content = f.read()
                                _file = {
                                    "path": item_path,
                                    "content": content,
                                    "visited": False
                                }
                                self.files.append(_file)
                                structure[item] = _file
                        except Exception as e:
                            _log.error(f'Could not read file {item_path}: {e}')
                            extension = os.path.splitext(item)[1]
                            self.matcher.add_ignore_pattern(f'*{extension}')
                            structure[item] = {}
        except Exception as e:
            _log.error(f'Error traversing path {path}: {e}')
        return structure


# Example usage:
codebase = DirectoryIngestor('../')
print(json.dumps(codebase.structure, indent=4))
