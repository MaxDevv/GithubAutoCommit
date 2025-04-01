#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module Description
------------------
A python script that traverses your base code folder and commits and pushes any repos with more than 5 changes.
Auto Commiting can be altered by adding the file NO_AUTO_COMMIT to the main repo.
"""

import sys
from typing import Optional, Any
import os, time, subprocess
# from numba import jit

# ===== Configuration =====
class Config:
    """Global settings (variables instead of constants)."""
    changeCriterion = 5 # Amount of changes needed before repo is commited and pushed
    mainCodeFolder = os.environ["CODE_FOLDER"]
    personalAccessToken = os.environ["GITHUB_PERSONAL_ACCESS_TOKEN"]
    verbose = True
    UseArgParse = False  # Enable to activate CLI parsing
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ===== Numba-Accelerated Functions =====
# @jit(nopython=True)
# def fastSquare(x: float) -> float:
#     """Compute x² (optimized with Numba)."""
#     return x * x

# ===== Main Class =====
class MainClass:
    """
    Core processing class with configurable workflow.
    """

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.result = None
    '''
    # ==== Function Boilerplate ====
    def func(self, variable: int = 69) -> None:
        """
        Description:
            - Describe this function
        Args:
            - variable,  an int representing a variable
        """
        if self.verbose:
            print("Initializing processor...")
    '''
    def checkGit(self, path: str) -> bool:
        """
        Description:
            - Checks if a folder represents a git repository
        Args:
            - Path, a folder path that leads to a folder
        """
        if self.verbose:
            print(f"Checking Repo, {path}")

        if not os.path.exists(os.path.join(path, ".git")):
            return False

        return True
    
    
    def findRepos(self, path: str) -> list:
        """
        Description:
            - Loops through all the subfolders in a given directory, and returns a list containing the path to all the subfolders that represent a github repo
        Args:
            - Path, a folder path that leads to a folder
        """
        repos = []
        
        if self.verbose:
            print(f"Searching for repos in {path} ...")
        
        for potentialRepo in os.listdir(path):
            fullPath = os.path.join(path, potentialRepo)
            if self.checkGit(fullPath):
                repos.append(fullPath)
        
        return repos
            
    
    def countChanges(self, repoPath: str) -> int:
        """
        Description:
            - determines how many changes have been made to a certain github repo
        Args:
            - Path, a folder path that leads to a folder representing a github repo
        """
        if self.verbose:
            print(f"Counting changes in repo: {repoPath}...")
        
        result = subprocess.run(["git", "status", "--porcelain"], cwd=repoPath, capture_output=True, text=True)
        changes = len(result.stdout.strip().split("\n")) if result.stdout.strip() else 0
        
        if self.verbose:
            print(f"{str(changes)} changes found in repo: {repoPath}...")
        
        return changes

    
    def commitAndPush(self, repoPath: str, commitMsg: str = f"Auto Commit, > {str(Config.changeCriterion)} uncommited changes made in 24 hour period") -> None:
        """
        Description:
            - commits and pushes a github repo
        Args:
            - Path, a folder path that leads to a folder representing a github repo
        """

        if self.verbose:
            print(f"Committing and pushing repo {repoPath} ...")
        
        subprocess.run(["git", "add", "-A"], cwd=repoPath)
        time.sleep(1)

        subprocess.run(["git", "commit", "-m", commitMsg], cwd=repoPath)
        time.sleep(1)

        branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repoPath, capture_output=True, text=True).stdout.strip()
        time.sleep(1)
        
        subprocess.run(["git", "push", "origin", branch], cwd=repoPath)
    
    
    def run(self) -> None:
        """
        Description:
            - Loops through all the files in the main code folder and commits and pushes all the repos with more than n changes.
        Args:
            - None.
        """
        

        for repo in self.findRepos(Config.mainCodeFolder):
            if os.path.exists(os.path.join(repo, "NO_AUTO_COMMIT")):
                if self.verbose:
                    print("Repo {repo}, contains flag NO_AUTO_COMMIT.")
                continue


            if self.countChanges(repo) >= Config.changeCriterion:
                self.commitAndPush(repo)

        pass

# ===== Main Function =====
def main() -> int:
    """Entry point with optional CLI args."""
    verbose = Config.verbose

    # ===== Optional CLI =====
    if Config.UseArgParse:
        import argparse
        parser = argparse.ArgumentParser(description="MainClass runner.")
        parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug mode")
        args = parser.parse_args()
        verbose = args.verbose

    # Run processor
    processor = MainClass(verbose=verbose)
    return processor.run()

if __name__ == "__main__":
    sys.exit(main())