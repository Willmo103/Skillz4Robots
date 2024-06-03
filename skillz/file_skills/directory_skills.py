# This module will consist of a collection of functions that will allow LLM's to interact with directories and files in
# a controlled manner. There will be a collection of data objects that will be used to store information about files and
# directories that will provide stateful information to help steer the LLM in the right direction. Examples of these
# objects are as follows:
# ====================================================================================================================
# File: <- Base class for all file objects
# ====================================================================================================================
#    requirements:
#       -numpy, FAISS, torch, transformers, sentence_transformers, sklearn,
#        scipy, pandas, yaml, json, os, re, datetime, typing, abc
#
# ====================================================================================================================
#    class description:
#       an abstract base class for all file objects.
#       purpose:
#          This class will provide a base class for all file objects. This class will be used to create a common interface
#          for all file objects that will be used by the LLM. This will allow the LLM to interact with files in a
#          consistent manner.
#       Fields:
#          - path: str - the path to the file
#          - parent: Directory | None - the parent directory of the file
#          - was_modified: bool - a flag to indicate if the LLM has modified the file
#          - was_read: bool - a flag to indicate if the LLM has read the file
#          - versions: list - a list of versions of the file
#          - content: str - the content of the file
#          - filename: str - the name of the file
#          - extension: str - the extension of the file
#       Initialization:
#          - __init__: -> None
#              - self
#              - path: str - the path to the file
#              - parent: Directory | None = None - the parent directory of the file
#              - description:
#                  initialize the file object
#              - procedure:
#                  This method takes the path to the file as the base argument and initializes the file object with the
#                  path and parent directory. The was_modified and was_read flags are set to False, the versions list is
#                  initialized as an empty list, and the content is set to an empty string. The filename and extension
#                  fields are set to the name and extension of the file respectively. The filename and extension fields
#                     set to the name and extension of the file respectively.
#       Methods:
#          - get_content: -> str
#              - self
#              - description:
#                  get the content of the file
#              - purpose:
#                  This method will be used to get the content of the file. If the content has not been read yet, the
#                  method will read the content from the file and set the was_read flag to True. If the content has been
#                  read before, the method will return the content from memory.
#          - update_content: -> None
#              - self
#              - content: str
#              - description:
#                  update the content of the file
#              - purpose:
#                  This method will be used to update the content of the file. The content argument will be used to set
#                  the content of the file. The was_modified flag will be set to True to indicate that the file has been
#                  modified and the previous content will be added to the versions list.
#          - get_version: -> str
#              - self
#              - version: int
#              - description:
#                  get a previous version of the file
#              - purpose:
#                  This method will be used to get a previous version of the file. The version argument will be used to
#                  determine which version of the file to return. If the version argument is 0, the current version of the
#                  file will be returned. If the version argument is greater than 0, the method will return the version of
#                  the file that corresponds to the version argument. If the version argument is less than 0, the method
#                  will return the version of the file that corresponds to the version argument from the end of the versions
#                  list.
#          - annotate: -> None
#              - self
#              - annotation: str
#              - description:
#                  annotate the file
#              - purpose:
#                  This method will be used to annotate the file. The annotation argument will be used to add an annotation
#                  to the file. The annotation will be added to the content of the file in a comment block at the top of the
#                  file.
#          - summarize: -> str
#              - self
#              - description:
#                  summarize the file
#              - purpose:
#                 This method will be used to attach a LLM generated summary to the file. The summary will be added to the
#                 content of the file in a comment block at the top of the file.
#          - tag_file: -> None
#              - self
#              - tag: str
#              - description:
#                  tag the file
#              - purpose:
#                  This method will be used to top of the file in a comment yaml block at the top of the file. ( using the Obsidian MD format)
#                  This will allow the LLM to tag the file with metadata that can be used to filter and search for files.
#
#          - create_embedding: -> None
#              - self
#              - description:
#                  create a vector embedding of the file
#              - purpose:
#                  This method will be used to create a vector embedding of the file. The embedding will be created using a
#                  pre-trained model and will be stored in the file object. The embedding will be used to compare the file
#                  to other files and directories in the LLM.
#          - get_embedding: -> np.array
#              - self
#              - description:
#                  get the vector embedding of the file
#              - purpose:
#                  This method will be used to get the vector embedding of the file. The embedding will be used to compare
#                  the file to other files and directories in the LLM.
#          - get_similarity: -> float
#              - self
#              - file: File
#              - description:
#                  get the similarity between the file and another file
#              - purpose:
#                  This method will be used to get the similarity between the file and another file. The similarity will be
#                  calculated using the vector embeddings of the files and will be returned as a float between 0 and 1.
#          - get_difference: -> float
#              - self
#              - file: File
#              - description:
#                  get the difference between the file and another file
#              - purpose:
#                  This method will be used to get the difference between the file and another file. The difference will be
#                  calculated using the vector embeddings of the files and will be returned as a float between 0 and 1.
#          - get_distance: -> float
#              - self
#              - file: File
#              - description:
#                  get the distance between the file and another file
#              - purpose:
#                  This method will be used to get the distance between the file and another file. The distance will be
#                  calculated using the vector embeddings of the files and will be returned as a float between 0 and 1.
#          - get_similarity_matrix: -> np.array
#              - cls
#              - files: list
#              - description:
#                  get a similarity matrix of a list of files
#              - purpose:
#                  This method will be used to get a similarity matrix of a list of files. The similarity matrix will be
#                  calculated using the vector embeddings of the files and will be returned as a numpy array.
#          - get_difference_matrix: -> np.array
#              - cls
#              - files: list
#              - description:
#                  get a difference matrix of a list of files
#              - purpose:
#                  This method will be used to get a difference matrix of a list of files. The difference matrix will be
#                  calculated using the vector embeddings of the files and will be returned as a numpy array.
#          - get_distance_matrix: -> np.array
#              - cls
#              - files: list
#              - description:
#                  get a distance matrix of a list of files
#              - purpose:
#                  This method will be used to get a distance matrix of a list of files. The distance matrix will be
#                  calculated using the vector embeddings of the files and will be returned as a numpy array.
#          - get_similarity_vector: -> np.array
#              - self | cls
#              - files: list
#              - description:
#                  get a similarity vector of a list of files
#              - purpose:
#                  This method will be used to get a similarity vector of a list of files. The similarity vector will be
#                  calculated using the vector embeddings of the files and will be returned as a numpy array.
#          - get_difference_vector: -> np.array
#              - self | cls
#              - files: list
#              - description:
#                  get a difference vector of a list of files
#              - purpose:
#                  This method will be used to get a difference vector of a list of files. The difference vector will be
#                  calculated using the vector embeddings of the files and will be returned as a numpy array.
#
# ====================================================================================================================
# Directory: <- Base class for all directory objects
# ====================================================================================================================
#    requirements:
#       -numpy, FAISS, torch, transformers, sentence_transformers, sklearn,
#        scipy, pandas, yaml, json, os, re, datetime, typing, abc
# ====================================================================================================================
#       description:
#          an abstract base class for all directory objects.
#      purpose:
#          This class will provide a base class for all directory objects. This class will be used to create a common
#          interface for all directory objects that will be used by the LLM. This will allow the LLM to interact with
#          directories in a consistent manner.
#      Fields:
#          - path: str - the path to the directory
#          - files: list - a list of Files in the directory
#          - directories: list - a list of Directories in the directory
#       - parent: Directory | None - the parent directory of the directory
#       - is_root: bool - a flag to indicate if the directory is the root directory
#   Initialize Methods:
#       - __init__: -> None
#           - self
#           - path: str - the path to the directory
#           - parent: Directory | None = None - the parent directory of the directory
#           - is_root: bool = True - a flag to indicate if the directory is the root directory
#
#           - description:
#               initialize the directory object
#           - procedure:
#             This method takes the path to the directory as the base argument and recursively builds the directory
#             structure by creating new directory and file objects along the way, so that the JSON object that is
#             produced by the serialize method will contain all directories as new objects containing all files and
#             subdirectories as new objects.
#        - from_json: -> Directory
#           - cls
#           - json: dict(JSON)
#           - write: bool = False
#           - write_path: str | None = None
#
#           - description:
#              create a directory object from a JSON object, optionally creating the directory on the file system
#           - procedure:
#              This method will take a JSON object that was created by the serialize method and create a directory
#              object from it. The write flag will determine if the directory is created on the file system. If the
#              write flag is set to True, the write_path argument will be used to determine the location of the
#              directory on the file system. If the write_path argument is not provided, the directory will be created
#              in the current working directory.
#
#        - create_directory: -> Directory
#           - cls
#           - path: str
#           - parent: Directory | None = None
#           - is_root: bool = False
#
#           - description:
#              create a directory object
#           - procedure:
#              This method will create a new directory object. The path argument will be used to determine the location
#              of the directory on the file system. The parent argument will be used to determine the parent directory
#              of the new directory. The is_root argument will be used to determine if the new directory is the root
#              directory.
#
#   Methods:
#      - serialize: -> dict(JSON)
#         description:
#            serialize the directory object to a dictionary
#         purpose:
#            This method will be used to serialize the directory object to a dictionary that can be converted to JSON
#            and stored in a file. This will allow the LLM to save the state of the directory object and load it back
#            in later.
#
#      - get_file: -> File
#         - self
#         - name: str
#         - recursive: bool = False
#
#         - description:
#            get a file object from the directory
#         - purpose:
#            This method will be used to get a file object from the directory. The name argument will be used to
#            determine which file to return. If the recursive flag is set to True, the method will search recursively
#            through all subdirectories to find the file. If the file is not found, the method will return None.
#      - get_files: -> list
#         - self
#         - recursive: bool = False
#         - description:
#            get a list of file objects from the directory
#         - purpose:
#            This method will be used to get a list of file objects from the directory. If the recursive flag is set to
#            True, the method will search recursively through all subdirectories to find all files. If no files are found,
#            the method will return an empty list.
#      - get_subdirectory: -> Directory
#         - self
#         - name: str
#         - recursive: bool = False
#         - description:
#            get a directory object from the directory
#         - purpose:
#            This method will be used to get a directory object from the directory. The name argument will be used to
#            determine which directory to return. If the recursive flag is set to True, the method will search recursively
#            through all subdirectories to find the directory. If the directory is not found, the method will return None.
#      - get_all_subdirectories: -> list
#         - self
#         - recursive: bool = False
#         - description:
#            get a list of directory objects from the directory
#         - purpose:
#            This method will be used to get a list of directory objects from the directory. If the recursive flag is set
#            to True, the method will search recursively through all subdirectories to find all directories. If no
#            directories are found, the method will return an empty list.
#      - add_file: -> None
#         - self
#         - file: File
#         - description:
#            add a file object to the directory
#         - purpose:
#            This method will be used to add a file object to the directory. The file argument will be used to determine
#            which file to add. If the file already exists in the directory, the method will update the file with the new
#            file object. If the file does not exist in the directory, the method will add the file to the directory.
#      - add_directory: -> None
#         - self
#         - directory: Directory
#         - description
#            add a directory object to the directory
#         - purpose:
#            This method will be used to add a directory object to the directory. The directory argument will be used to
#            determine which directory to add. If the directory already exists in the directory, the method will update
#            the directory with the new directory object. If the directory does not exist in the directory, the method
#            will add the directory to the directory.
#      - remove_file: -> None
#         - self
#         - name: str
#         - recursive: bool = False
#         - description:
#            remove a file object from the directory
#         - purpose:
#            This method will be used to remove a file object from the directory. The name argument will be used to
#            determine which file to remove. If the recursive flag is set to True, the method will search recursively
#            through all subdirectories to find the file. If the file is not found, the method will return None.
#      - remove_directory: -> None
#         - self
#         - name: str
#         - recursive: bool = False
#         - description:
#            remove a directory object from the directory
#         - purpose:
#            This method will be used to remove a directory object from the directory. The name argument will be used to
#            determine which directory to remove. If the recursive flag is set to True, the method will search recursively
#            through all subdirectories to find the directory. If the directory is not found, the method will return None.
#      - update_file: -> None
#         - self
#         - name: str
#         - file: File
#         - description:
#            update a file object in the directory
#         - purpose:
#            This method will be used to update a file object in the directory. The name argument will be used to
#            determine which file to update. The file argument will be used to determine the new file object. If the file
#            does not exist in the directory, the method will return None.
#      - update_directory: -> None
#         - self
#         - name: str
#         - directory: Directory
#         - description:
#            update a directory object in the directory
#         - purpose:
#            This method
#            will be used to update a directory object in the directory. The name argument will be used to determine
#            which directory to update. The directory argument will be used to determine the new directory object. If the
#            directory does not exist in the directory, the method will return None.
#      - move_file: -> None
#         - self
#         - name: str
#         - new_directory: Directory
#         - description:
#            move a file object to a new directory
#         - purpose:
#            This method will be used to move a file object to a new directory. The name argument will be used to
#            determine which file to move. The new_directory argument will be used to determine the new directory to
#            move the file to. If the file does not exist in the directory, the method will return None.
#      - move_directory: -> None
#         - self
#         - name: str
#         - new_directory: Directory
#         - description:
#            move a directory object to a new directory
#         - purpose:
#            This method will be used to move a directory object to a new directory. The name argument will be used to
#            determine which directory to move. The new_directory argument will be used to determine the new directory to
#            move the directory to. If the directory does not exist in the directory, the method will return None.
#      - copy_file: -> None
#         - self
#         - name: str
#         - new_directory: Directory
#         - description:
#            copy a file object to a new directory
#         - purpose:
#            This method will be used to copy a file object to a new directory. The name argument will be used to
#            determine which file to copy. The new_directory argument will be used to determine the new directory to
#            copy the file to. If the file does not exist in the directory, the method will return None.
#      - copy_directory: -> None
#         - self
#         - name: str
#         - new_directory: Directory
#         - description:
#            copy a directory object to a new directory
#         - purpose:
#            This method will be used to copy a directory object to a new directory. The name argument will be used to
#            determine which directory to copy. The new_directory argument will be used to determine the new directory to
#            copy the directory to. If the directory does not exist in the directory, the method will return None.
#      - create_file: -> File
#         - self
#         - name: str
#         - content: str = ''
#         - description:
#            create a file object in the directory
#         - purpose:
#            This method will be used to create a file object in the directory. The name argument will be used to
#            determine the name of the new file. The content argument will be used to determine the content of the new
#            file.
#      - create_directory: -> Directory
#         - self
#         - name: str
#         - description:
#            create a directory object in the directory
#         - purpose:
#            This method will be used to create a directory object in the directory. The name argument will be used to
#            determine the name of the new directory.
#
# ====================================================================================================================
# Codebase( Directory ) <- A class that will be used to represent a codebase directory. This class will be used to
#                          represent a directory that contains a collection of code files, and a git interface that will
#                          allow the LLM to interact with the codebase in a controlled manner.
# ====================================================================================================================
#    requirements:
#       -numpy, FAISS, torch, transformers, sentence_transformers, sklearn,
#        scipy, pandas, yaml, json, os, re, datetime, typing, abc
# ====================================================================================================================
#    class description:
#       a class that will be used to represent a codebase directory
#    purpose:
#       This class will be used to represent a codebase directory. This class will be used to represent a directory that
#       contains a collection of code files, and a git interface that will allow the LLM to pull repositories as requested
#       and interact with the codebase in a guided and controlled manner.
#    Unique Fields:
#       - remote_url: str - the remote URL of the codebase
#       - branch: str - the current branch of the codebase
#       - ignored_files: list - a list of files that are to be ignored entirely by code and llm (e.g. __pycache__, .git, venv, etc.)
#       - git: Git - a git interface for the codebase
#    Initialize Methods:
#       - __init__: -> None (super init)
#           - self
#           - path: str - the path to the directory
#           - parent: Directory | None = None - the parent directory of the directory
#           - is_root: bool = True - a flag to indicate if the directory is the root directory
#           - remote_url: str = None - the remote URL of the codebase
#           - branch: str = 'master' - the current branch of the codebase
#          - description:
#             initialize the codebase object
#          - procedure:
#             This method takes the path to the directory as the base argument and recursively builds the directory
#             structure by creating new directory and file objects along the way, so that the JSON object that is
#             produced by the serialize method will contain all directories as new objects containing all files and
#             subdirectories as new objects. The remote_url argument will be used to determine the remote URL of the
#             codebase. The branch argument will be used to determine the current branch of the codebase. The ignored_files
#             list will be used to determine which files to ignore entirely by code and llm.
#    Methods:
#       - pull: -> None
#          - self
#          - description:
#             pull the latest changes from the remote repository
#          - purpose:
#             This method will be used to pull the latest changes from the remote repository. The method will use the git
#             interface to pull the latest changes from the remote repository and update the codebase with the new changes.
#       - _push: -> None
#          - self
#          - description:
#             push the changes to the remote repository
#          - purpose:
#             This method will be used to push the changes to the remote repository. The method will use the git interface
#             to push the changes to the remote repository and update the remote repository with the new changes.
#       - _commit: -> None
#          - self
#          - message: str
#          - description:
#             commit the changes to the local repository
#          - purpose:
#             This method will be used to commit the changes to the local repository. The message argument will be used to
#             determine the commit message that will be associated with the changes. The method will use the git interface
#             to commit the changes to the local repository and update the local repository with the new changes.
#       - _add: -> None
#          - self
#          - description:
#             add the changes to the local repository
#          - purpose:
#             This method will be used to add the changes to the local repository. The method will use the git interface
#             to add the changes to the local repository and update the local repository with the new changes.
#       - _checkout: -> None
#          - self
#          - branch: str
#          - description:
#             checkout a branch in the local repository
#          - purpose:
#             This method will be used to checkout a branch in the local repository. The branch argument will be used to
#             determine which branch to checkout. The method will use the git interface to checkout the branch in the local
#             repository and update the local repository with the new branch.
#       - _pull: -> None
#          - self
#          - description:
#             pull the latest changes from the remote repository
#          - purpose:
#             This method will be used to pull the latest changes from the remote repository. The method will use the git
#             interface to pull the latest changes from the remote repository and update the codebase with the new changes.
#       - iter_all_files: -> File
#          - self
#          - description:
#            iterate over all files in the codebase directory This is helpful for summarization tasks, or understanding etc.
#          - purpose:
#            This method will be used to iterate over all files in the codebase directory. The method will yield a file
#            object for each file in the codebase directory.
#       - pip_install: -> None
#          - self
#          - package: str
#          - description:
#             install a package in the codebase
#          - purpose:
#             This method will be used to install a package in the codebase. The package argument will be used to determine
#             which package to install. The method will use the pip interface to install the package in the codebase.
#       - pip_uninstall: -> None
#          - self
#          - package: str
#          - description:
#             uninstall a package in the codebase
#          - purpose:
#             This method will be used to uninstall a package in the codebase. The package argument will be used to determine
#             which package to uninstall. The method will use the pip interface to uninstall the package in the codebase.
#       - pip_list: -> list
#          - self
#          - description:
#             list all installed packages in the codebase
#          - purpose:
#             This method will be used to list all installed packages in the codebase. The method will use the pip interface
#             to list all installed packages in the codebase and return a list of installed packages.
#       - create_requirements: -> None
#          - self
#          - description:
#             create a requirements file for the codebase
#          - purpose:
#             This method will be used to create a requirements file for the codebase. The method will use the pip interface
#             to list all installed packages in the codebase and write the list of installed packages to a requirements file.
#       - install_requirements: -> None
#          - self
#          - description:
#             install all requirements in the codebase
#          - purpose:
#             This method will be used to install all requirements in the codebase. The method will use the pip interface
#             to install all requirements in the codebase from the requirements file.
#       - create_environment: -> None
#          - self
#          - description:
#             create a virtual environment for the codebase
#          - purpose:
#             This method will be used to create a virtual environment for the codebase. The method will use the venv
#             interface to create a virtual environment in the codebase and activate the virtual environment.
#       - activate_environment: -> None
#          - self
#          - description:
#             activate the virtual environment for the codebase
#          - purpose:
#             This method will be used to activate the virtual environment for the codebase. The method will use the venv
#             interface to activate the virtual environment in the codebase.
#       - deactivate_environment: -> None
#          - self
#          - description:
#             deactivate the virtual environment for the codebase
#          - purpose:
#             This method will be used to deactivate the virtual environment for the codebase. The method will use the venv
#             interface to deactivate the virtual environment in the codebase.
#       - run_tests: -> None
#          - self
#          - description:
#             run the tests in the codebase
#          - purpose:
#             This method will be used to run the tests in the codebase. The method will use the pytest interface to run
#             the tests in the codebase and return the results of the tests.

# ====================================================================================================================4
# Skills to implement:
# - TBD

import os


class File:
    def __init__(self, path: str, parent: Directory | None = None):
        if os.path.exists(path) and not os.path.isfile(path):
            self.path: str = path
            self.parent: Directory = parent
            self.was_modified = False
            self.was_read = False
            self.versions: list[str] = []
            self.summary: str = ""
            self.content: str = ""
            self.tags: list[str] = []
            self.filename: str = os.path.basename(path)
            self.extension: str = os.path.splitext(path)[1]
        else:
            raise ValueError(f"Path {path} does not exist or is not a file.")

    def get_content(self) -> str:
        if not self.was_read:
            with open(self.path, "r") as f:
                self.content = f.read()
            self.was_read = True
        return self.content

    def update_content(self, content: str) -> None:
        self.versions.append(self.content)
        self.content = content
        self.was_modified = True

    def get_version(self, version: int) -> str:
        if version == 0:
            return self.content
        elif version > 0:
            return self.versions[version - 1]
        else:
            return self.versions[version]

    def annotate(self, annotation: str) -> None:
        self.content = f"/* {annotation} */\n" + self.content

    def summarize(self, summary: str) -> None:
        self.summary = summary

    def tag_file(self, tag: str) -> None:
        self.tags.append(tag)

    def create_embedding(self) -> None:
        ...


class Directory:
    def __init__(self, path: str, parent: Directory | None = None, is_root: bool = True):  # noqa
        if os.path.exists(path) and os.path.isdir(path):
            self.path: str = path
            self.files: list[File] = []
            self.directories: list[Directory] = []
            self.parent: Directory = parent
            self.is_root: bool = is_root
        else:
            raise ValueError(
                f"Path {path} does not exist or is not a directory.")

    def serialize(self) -> dict:
        return {
            "path": self.path,
            "files": [file.serialize() for file in self.files],
            "directories": [directory.serialize() for directory in self.directories],
            "is_root": self.is_root
        }

    def get_file(self, name: str, recursive: bool = False) -> File:
        for file in self.files:
            if file.filename == name:
                return file
        if recursive:
            for directory in self.directories:
                file = directory.get_file(name, recursive)
                if file:
                    return file
        return None

    def get_files(self, recursive: bool = False) -> list[File]:
        files = self.files
        if recursive:
            for directory in self.directories:
                files.extend(directory.get_files(recursive))
        return files

    def get_subdirectory(self, name: str, recursive: bool = False) -> Directory:
        for directory in self.directories:
            if directory.path == name:
                return directory
        if recursive:
            for directory in self.directories:
                subdirectory = directory.get_subdirectory(name, recursive)
                if subdirectory:
                    return subdirectory
        return None

    def get_all_subdirectories(self, recursive: bool = False) -> list[Directory]:
        directories = self.directories
        if recursive:
            for directory in self.directories:
                directories.extend(directory.get_all_subdirectories(recursive))
        return directories

    def add_file(self, file: File) -> None:
        for f in self.files:
            if f.filename == file.filename:
                self.files.remove(f)
                break
        self.files.append(file)

    def add_directory(self, directory: Directory) -> None:
        for d in self.directories:
            if d.path == directory.path:
                self.directories.remove(d)
                break
        self.directories.append(directory)

    def remove_file(self, name: str, recursive: bool = False) -> None:
        for file in self.files:
            if file.filename == name:
                self.files.remove(file)
                return
        if recursive:
            for directory in self.directories:
                directory.remove_file(name, recursive)
