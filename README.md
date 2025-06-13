#CheckKernal – Linux Kernel Security Inspector

**CheckKernal** is a lightweight Python tool for analyzing critical Linux kernel security configurations.
It generates structured `JSON` and visual `HTML` reports suitable for audits, DFIR, threat hunting, and pentesting.

#Features

- Detects current kernel version and user information
- Outputs structured reports:
  - `output.json`
  - `output.html`

#Installation

```bash
git clone https://github.com/SeniorMohamed/CheckKernal.git
cd CheckKernal
python3 checkkernal.py
