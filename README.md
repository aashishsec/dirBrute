# dirBrute - Directory Brute Forcing Tool

[Tool Link](https://github.com/aashishsec/dirBrute/)
---

![GitHub last commit](https://img.shields.io/github/last-commit/aashishsec/dirBrute) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/aashishsec/dirBrute) [![GitHub license](https://img.shields.io/github/license/aashishsec/dirBrute)](https://github.com/aashishsec/dirBrute/blob/main/LICENSE) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/aashishsec/)

## Overview

- DirBrute is a powerful directory brute-forcing tool designed for efficient web application security testing.
  
- It's a go-to for uncovering hidden paths and directories, providing valuable insights into potential vulnerabilities.

- The Output contains with statuscode and content length.

- This DirBrute tool also had threading which will speed up the process.
  
-  Works in all platforms.
- 
## Features

1. **User-Agent Rotation:**
   - Randomly selects a user agent from a predefined list for each HTTP request to avoid detection.

2. **Colorized Output:**
   - Utilizes the `colorama` library to provide colorized and visually appealing output.

3. **Multithreading:**
   - Implements multithreading using Python's `concurrent.futures` module for concurrent execution of HTTP requests.

4. **HTTP Client:**
   - Utilizes the `httpx` library as the HTTP client with SSL certificate verification disabled.

5. **Command-Line Interface (CLI):**
   - Accepts command-line arguments through the `argparse` module for easy configuration.

6. **Output File:**
   - Saves results to an output file specified by the user (default: "httpAlive_output.txt").

7. **Banner Display:**
   - Displays a colorful banner at the beginning with information about the tool, author, and GitHub profile.

8. **Exception Handling:**
   - Includes exception handling to gracefully handle interruptions, such as `KeyboardInterrupt`.
     

## Installation

- Clone the repository to your local machine.
  
- Install the required dependencies using pip


```bash
git clone https://github.com/aashish36/dirBrute.git

cd dirBrute

pip install -r requirements.txt

```

## Usage

- Create a file containing that contains list of URLs or subdoamins or both and give to httpAlive. The output contains status codes and content length.

- This python code will save the results of the analysis to a file named 'dirBrute.txt'.

- Run the script using the following command: 

``` bash

DirBrute is a tool designed to efficiently probe for alive endpoints from a provided wordlist list.

options:

  -h, --help            show this help message and exit.

  -d list, --Domain list
                        [INFO]: domain.

  -w list, --wordlist list
                        [INFO]: List of wordlist.

  -o output, --output output
                        [INFO]: File to save our output.

  -c CONCURRENCY, --concurrency CONCURRENCY
                        [INFO]: Concurrency level to make fast process

  -t THREADS, --threads THREADS
                        [INFO]: Threading level to make fast process
```

## Tool Output

![image](https://github.com/aashishsec/dirBrute/assets/65489287/829cd513-86ca-489a-af52-79a6fef0596d)


## Contributing

- Contributions are welcome!
  
- If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
  
![image](https://github.com/aashish36/JSScanner/assets/65489287/70f7e3a8-e95f-429b-9433-89087daad721)
