# GithubAutoCommit

A Python utility that automatically commits and pushes changes to all your Git repositories.

## Description

GithubAutoCommit is a simple automation tool that traverses through your code folders, identifies Git repositories, and automatically commits and pushes any repositories with more than a specified number of changes. This tool is designed to be run via cron job or other automation methods to ensure your work is regularly committed.

## Features

- Automatically scans a base code folder for Git repositories
- Commits and pushes repositories with more than 3 changes (configurable)
- Skip repositories by adding a `NO_AUTO_COMMIT` file to the repository
- Designed to be run via automation (curl, cron jobs, etc.)
- No front-end UI required

## Requirements

- Python 3.x
- Git installed and configured
- Environment variables:
  - `CODE_FOLDER`: Path to your main code directory
  - `GITHUB_PERSONAL_ACCESS_TOKEN`: Your GitHub personal access token

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MaxDevv/GithubAutoCommit.git
```

2. Set up the required environment variables:
```bash
export CODE_FOLDER="/path/to/your/code/folder"
export GITHUB_PERSONAL_ACCESS_TOKEN="your-github-token"
```

## Usage

Simply run the main script:

```bash
python main.py
```

### Automation

To automate with cron:

```bash
# Add to crontab to run daily at midnight
0 0 * * * cd /path/to/GithubAutoCommit && python main.py
```

### Configuration

Edit the `Config` class in `main.py` to customize:
- `changeCriterion`: Minimum number of changes required before committing (default: 3)
- `verbose`: Enable/disable detailed logging

### Excluding Repositories

To exclude a repository from automatic commits, create an empty file named `NO_AUTO_COMMIT` in the repository's root directory.

## License

MIT License

Copyright (c) 2025 MaxDevv

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Made with <3 by MaxDevv :D