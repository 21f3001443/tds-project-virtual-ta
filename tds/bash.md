## Terminal: Bash

UNIX shells are the de facto standard in the data science world and [Bash](https://www.gnu.org/software/bash/) is the most popular.
This is available by default on Mac and Linux.

On Windows, install [Git Bash](https://git-scm.com/downloads) or [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) to get a UNIX shell.

Watch this video to install WSL (12 min).

[![How to Install Ubuntu on Windows 10 (WSL) (12 min)](https://i.ytimg.com/vi_webp/X-DHaQLrBi8/sddefault.webp)](https://youtu.be/X-DHaQLrBi8
<youtube_summary>To enable and use the Windows Subsystem for Linux (WSL) on Windows 10, follow these steps:

1. Open Control Panel, go to "Programs" > "Programs and Features," then click "Turn Windows features on or off." Alternatively, search directly for "Turn Windows features on or off."
2. In the list, check "Windows Subsystem for Linux" and click OK. After the changes are applied, restart your computer.
3. After reboot, open Command Prompt (cmd) and type "bash" to check WSL status. If no Linux distribution is installed, you will get a prompt with a URL.
4. Open Microsoft Store, search for a Linux distribution (e.g., Ubuntu, Kali Linux, Debian, SUSE Linux), and install your preferred one (Ubuntu is recommended).
5. Launch the installed Linux app (e.g., Ubuntu) from the Start menu or "Recently added" section.
6. On first launch, the Linux terminal will complete installation, then prompt you to create a Unix username and password (different from your Windows credentials).
7. After setup, you will get a Linux command prompt. You can use common Linux commands like `ls -al` and `pwd`.
8. To access your Windows drives from Linux, navigate to `/mnt/` (e.g., C: drive is `/mnt/c`).
9. You can traverse Windows directories and create files using Linux commands. For example, navigate to your desktop and create a file using `touch test.txt`.
10. Edit files with the `nano` editor, save, and view content with `cat`.
11. You can also run the Linux bash shell from Windows Command Prompt by typing `bash`.

This process allows you to run Linux commands and use a Linux environment natively within Windows 10 through WSL.</youtube_summary>
)

Watch this video to understand the basics of Bash and UNIX shell commands (75 min).

[![Beginner's Guide to the Bash Terminal (75 min)](https://i.ytimg.com/vi_webp/oxuRxtrO2Ag/sddefault.webp)](https://youtu.be/oxuRxtrO2Ag
<youtube_summary>This video is a beginner's crash course guide to using the Bash terminal on Linux, aimed at demystifying what many new users find intimidating. While Linux can be used entirely with graphical user interfaces (GUIs), Bash—the command-line shell—is powerful and often essential for troubleshooting and advanced tasks. The presenter emphasizes that the terminal assumes users know what they want to do and offers less intuitive guidance than a GUI, so caution is advised to avoid damaging the system.

Key topics covered include:

1. **Basic Navigation and Commands**:
   - `ls`: Lists files and directories in the current directory.
   - `pwd`: Prints the full path of the current directory.
   - Understanding absolute (full) and relative paths.
   - Using `cd` to change directories, including shortcuts like `cd` to go home, `cd ..` to go up one level, and tab autocomplete to speed typing.
   - Introduction to `pushd` and `popd` to switch between directories without losing place.

2. **Linux File System Structure**:
   - Root directory `/` as the base of the filesystem tree.
   - Home directories (e.g., `/home/username`) as locations for user files.
   - Directories and folders are interchangeable terms.

3. **File and Directory Management**:
   - Creating directories with `mkdir`.
   - Creating files with `touch` (creates empty files or updates timestamps).
   - Copying files with `cp`.
   - Renaming or moving files with `mv`.
   - Removing files with `rm` (with warnings about its power and irreversibility).
   - Removing empty directories with `rmdir`.
   - Recursive removal of directories and contents with `rm -r`.

4. **Viewing and Editing Files**:
   - Viewing file contents with `cat`.
   - Paging through long files with `more` and `less` (less is more advanced).
   - Editing files using the `nano` text editor, including saving and exiting.
   - Using redirection (`>`, `>>`) and piping (`|`) to send output to files or other commands.

5. **Finding Files and Commands**:
   - Using `locate` to find files by name (requires an updated database via `sudo updatedb`).
   - Using `which` to find the path of installed commands.
   - Using `history` and arrow keys to recall previously issued commands.

6. **Getting Help**:
   - `whatis` to get a brief description of a command.
   - `apropos` to search for commands related to a keyword.
   - `man` pages for detailed command documentation.

7. **User and Permission Management**:
   - Understanding the prompt information: username, hostname, current directory, and user privileges (indicated by `$` for regular users and `#` for root).
   - Using `sudo` to run commands with administrative privileges.
   - Using `su` to switch users or become root (with cautions about security and best practices).
   - Commands to see who is logged in (`users`) and to get user info (`id`).
   - Explanation of Linux file permissions: read (r), write (w), execute (x) for user, group, and others.
   - Changing permissions with `chmod` using symbolic (`+x`) and numeric methods (e.g., 755, 644).
   - Differences in permission handling between files and directories.

8. **Process Management**:
   - Stopping running commands in the terminal with `Ctrl+C`.
   - Killing processes by name with `killall`.
   - Using `which` to find executable names if unsure.

9. **Exiting the Terminal**:
   - Exiting sessions with `exit` or `Ctrl+D`.
   - Logging out properly, especially on real terminals or TTYs.

10. **Terminal Emulator Tips**:
    - Clearing/redrawing the screen with `Ctrl+L`.
    - Changing text size with `Ctrl+Shift++` (increase) and `Ctrl+-` (decrease) in most terminal emulators.

The video encourages viewers to practice by creating directories and files, experimenting with commands, and exploring more advanced topics as they grow comfortable. It highlights that Bash is universal across many systems, including Linux distributions and even Windows, making the skills widely applicable.

Additional resources mentioned include freedompenguin.com, Easy Linux website and Facebook page, and downloadable wallpapers.

The presenter reassures that though the terminal may seem daunting at first, with practice and use of the commands and concepts introduced, users can become proficient and leverage its power effectively.</youtube_summary>
)

Essential Commands:

```bash
# File Operations
ls -la               # List all files with details
cd path/to/dir       # Change directory
pwd                  # Print working directory
cp source dest       # Copy files
mv source dest       # Move/rename files
rm -rf dir           # Remove directory recursively

# Text Processing
grep "pattern" file  # Search for pattern
sed 's/old/new/' f   # Replace text
awk '{print $1}' f   # Process text by columns
cat file | wc -l     # Count lines

# Process Management
ps aux               # List processes
kill -9 PID          # Force kill process
top                  # Monitor processes
htop                 # Interactive process viewer

# Network
curl url             # HTTP requests
wget url             # Download files
nc -zv host port     # Test connectivity
ssh user@host        # Remote login

# Count unique values in CSV column
cut -d',' -f1 data.csv | sort | uniq -c

# Quick data analysis
awk -F',' '{sum+=$2} END {print sum/NR}' data.csv  # Average
sort -t',' -k2 -n data.csv | head                  # Top 10

# Monitor log in real-time
tail -f log.txt | grep --color 'ERROR'
```

Bash Scripting Essentials:

```bash
#!/bin/bash

# Variables
NAME="value"
echo $NAME

# Loops
for i in {1..5}; do
    echo $i
done

# Conditionals
if [ -f "file.txt" ]; then
    echo "File exists"
fi

# Functions
process_data() {
    local input=$1
    echo "Processing $input"
}
```

Productivity Tips:

1. **Command History**

   ```bash
   history         # Show command history
   Ctrl+R         # Search history
   !!             # Repeat last command
   !$             # Last argument
   ```

2. **Directory Navigation**

   ```bash
   pushd dir      # Push directory to stack
   popd           # Pop directory from stack
   cd -           # Go to previous directory
   ```

3. **Job Control**

   ```bash
   command &      # Run in background
   Ctrl+Z         # Suspend process
   bg             # Resume in background
   fg             # Resume in foreground
   ```

4. **Useful Aliases** - typically added to `~/.bashrc`
   ```bash
   alias ll='ls -la'
   alias gs='git status'
   alias jupyter='jupyter notebook'
   alias activate='source venv/bin/activate'
   ```
