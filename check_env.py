import sys
import subprocess

try:
    import lunardate
except ImportError:
    with open("/tmp/chinese_lunar_debug.log", "a") as f:
        f.write("lunardate not found\n")
    sys.exit(1)

with open("/tmp/chinese_lunar_debug.log", "a") as f:
    f.write(f"Python executable: {sys.executable}\n")
    f.write(f"sys.path: {sys.path}\n")
    f.write(f"lunardate version: {lunardate.__version__ if hasattr(lunardate, '__version__') else 'unknown'}\n")

print("lunardate imported successfully")

