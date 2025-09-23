from pathlib import Path

CurrentPath = Path(__file__).resolve()
print(CurrentPath.parent.parent/"Testcases"/"filetest.py")
print(__file__)
