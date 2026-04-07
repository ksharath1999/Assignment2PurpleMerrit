import subprocess

def run_test(file):
    result = subprocess.run(["python", file], capture_output=True, text=True)
    return result.stdout + result.stderr