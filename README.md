# dirBrute

- DirBrute is a tool designed to efficiently probe for alive endpoints from a provided wordlist list.

- The Output contains with statuscode and content length.

- This DirBrute tool also had threading which will speed up the process.
  
-  Works in all platforms.

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

![image](https://github.com/aashishsec/dirBrute/assets/65489287/a5f75f03-0542-41b7-bdee-ce38bc3a6331)


## Contributing

- Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

![image](https://github.com/aashish36/JSScanner/assets/65489287/70f7e3a8-e95f-429b-9433-89087daad721)
