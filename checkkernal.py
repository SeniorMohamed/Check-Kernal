# MIT License - See LICENSE file for full details
# Copyright (c) 2025 Mohamed Nagy
# Version 1.01

import platform
import json
from datetime import datetime

def get_kernel_info():
    return {
        "kernel_version": platform.uname().release,
        "system": platform.system(),
        "node_name": platform.node(),
        "release_time": datetime.utcnow().isoformat() + "Z"
    }

def save_report(data):
    with open("output.json", "w") as f:
        json.dump(data, f, indent=4)

    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Kernel Security Report</title>
    <style>
        body {{ font-family: Arial; background-color: #f4f4f4; padding: 20px; }}
        pre {{ background: #fff; padding: 15px; border-radius: 5px; }}
    </style>
</head>
<body>
    <h1>CheckKernal Security Report</h1>
    <pre>{json.dumps(data, indent=4)}</pre>
    <p><a href="https://ko-fi.com/drrobot" target="_blank">
    <button>Support Me if You Liked the Tool</button></a></p>
</body>
</html>
"""
    with open("output.html", "w") as f:
        f.write(html)

if __name__ == "__main__":
    info = get_kernel_info()
    save_report(info)
    print("Reports generated: output.json & output.html")
