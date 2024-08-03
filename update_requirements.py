import subprocess
import re


def get_latest_version(package_name):
    result = subprocess.run(
        ["pip", "install", f"{package_name}==random"],
        stderr=subprocess.PIPE,
        text=True
    )
    match = re.search(r'from versions: (.+)', result.stderr)
    if match:
        versions = match.group(1).split(', ')
        return versions[-1]
    return None


def update_requirements(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    updated_lines = []
    for line in lines:
        if '==' in line:
            package_name = line.split('==')[0]
            latest_version = get_latest_version(package_name)
            if latest_version:
                updated_lines.append(f"{package_name}=={latest_version}\n")
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
    
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)


if __name__ == "__main__":
    update_requirements('requirements.txt')
