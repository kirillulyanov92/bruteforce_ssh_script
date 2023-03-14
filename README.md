# Bruteforce SSH

This python script uses the [Paramiko library](https://pypi.org/project/paramiko/) to attempt an SSH connection with the specified username and password combination for the given IP address. If a valid combination is found, it prints it to the screen and exits the program. If no valid combinations are found, it prints a message indicating this.

> **Warning**
>
> Please note that this script is for educational purposes only and should not be used for malicious activities. Additionally, brute-forcing SSH logins is illegal in many jurisdictions and can lead to severe consequences.

## Installation

Fork this repository by clicking the "fork" button on the top right of the homepage of this repo.
Now, go to the forked repository and click on the green `clone or download` button. Copy the url.
Go to your command line and go to the directory where you want to clopository. Then type `git clone` followed by the url you copied:

    git clone https://github.com/kirillulyanov92/bruteforce_ssh_script.git
    
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install paramiko.

```bash
pip install paramiko
pip install threading
```

## Usage

```bash
python3 main.py

# input path username.txt

# input path password.txt

# input ip's target
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
