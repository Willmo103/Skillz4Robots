from typing import Callable


def run_tests(tests: list, module_name: str | None = None) -> list:
    results = []
    if module_name:
        print(f"Running tests from {module_name}\n")
    else:
        print("Running tests\n")
    for test in tests:
        result = test()
        results.append((test.__name__, result[0], result[1]))
        print(result[0], end="", flush=True)
    print("  Done!\n")
    print("\n==========+\n  Results\n==========+\n")
    for i, result in enumerate(results):
        print(
            f"\n{i}. {tests[i].__name__}\nResult: {'Passed' if result[1] not in ['F', '!'] else 'Failed'}\nReturned: {result[2]}"
        )
    if module_name:
        print(f"\nTests from {module_name} complete!")
    else:
        print("\nTests complete!")
    return results

#
# class SkillTest:
#     def __init__(
#             self,
#             test: Callable,
#             test_name: str,
#             test_description: str | None = None,
#             test_module: str | None = None
#     ):
#         self.test = test
#         self.test_name = test_name
#         self.test_description = test_description if test_description else ""
#         self.test_module = test_module if test_module else ""
#         self.result = None
#         self.error = None
#         self.status = None
#
#     def __call__(self):
#         try:
#             self.result = self.test()
#             self.status = "."
#         except AssertionError as e:
#             self.error = str(e)
#             self.status = "F"
#         except Exception as e:
#             self.error = str(e)
#             self.status = "!"
#         return self.status, self.result[1]