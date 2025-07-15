# analyzer.py
log_file = 'sample.log'

info_count = 0
warning_count = 0
error_count = 0

with open(log_file, 'r') as f:
    lines = f.readlines()

    for line in lines:
        if 'ERROR' in line:
            error_count += 1
        elif 'WARNING' in line:
            warning_count += 1
        elif 'INFO' in line:
            info_count += 1

print(f"Total Lines: {len(lines)}")
print(f"INFO: {info_count}, WARNING: {warning_count}, ERROR: {error_count}")
