# Cryptography Practice - - Cipher.py

This is a simple Python Program developed to allow the encryption and decryption of user supplied plaintext via a variety of simple ciphers.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Note: this program was built and optimized for Python 3.x - we recommend Python Version=3.8.5 

### Prerequisites

Only Python 3 is essential for running this program, as all the packages used (sys, string, random, and argparse)
are part of the standard library

Python libraries used by this program:

```
sys
string
random
argparse
```
If you already know you have an appropriate version of Python installed on your system, you can skip to [Usage](#usage).

If you know you're missing Python3, you can find download the appropriate package for your OS via the link below.
If you're unsure, or you have never installed Python before check out the next section about installing python.

* [Python.org](https://www.python.org/getit/) - Get Python 3.x here



## Installing

First check to see if Python is installed on your system and if so, what version is running. 
How that process works depends largely on your Operating System (OS).

### Linux

Note: Most Linux distributions come with Python preloaded, but it might not be with the latest version
 and you could only have Python 2 instead of Python 3 (which is what this program is written in).
 Double check your system's version by using the following commands:
```
# Check the system Python version
$ python --version

# Check the Python 2 version
$ python2 --version

# Check the Python 3 version
$ python3 --version
```

### Windows

In windows, open ‘cmd’ (Command Prompt) and type the following command.

```
C:\> python --version

```
Using the --version switch will show you the version that’s installed. Alternatively, you can use the -V switch:
```
C:\> python -V

```
Either of the above commands will give the version number of the Python interpreter installed or they will display an error if otherwise.

### Mac OSX

Starting with Catalina, Python no longer comes pre-installed on most Mac computers, and many older models only
have Python 2 pre-installed, not Python 3. In order to check the Python version currently installed on your Mac,
open a command-line application, i.e. Terminal, and type in any of the following commands:

```
# Check the system Python version
$ python --version

# Check the Python 2 version
$ python2 --version

# Check the Python 3 version
$ python3 --version
```
Note:
You’ll want to either download or upgrade to the latest version of Python if any of the following conditions are true:
* None of the above commands return a version number on your machine.
* The only versions you see listed when running the above commands are part of the Python 2.x series.
* Your version of Python 3 isn’t the latest available, which was version 3.8.5 as writing this.

If Python is not already on your system, or it is not version 3.6x or above, you can find
detailed installation instructions for your particular OS, here:

Detailed instructions for installing Python3 on Linux, MacOS, and Windows, are available at link below:

* [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/) - How to install Python3

## Usage

Once you have verified that you have Python 3.x installed and running on your system, using this program is
fairly straight forward. In the same command (or terminal) window that you checked the version number of Python,
run 'python cipher.py -h' - as shown below there are also a couple of optional arguments:

```
usage: cipher.py [-h] [-E] [-D] [-f] [-i INPUTFILE] [-o OUTPUTFILE]
                 [-S {left,right}] [-T {Caesar,Substitution,Vigenere}]

 optional arguments:
  -h, --help            show this help message and exit
  -E, --encrypt         Signals that user wants to encrypt text.
  -D, --decrypt         Signals that user wants to decrypt text.
  -f, --file            File used as source with results saved to new File.
  -i INPUTFILE, --input_from_file INPUTFILE
                        Load text from the provided file name.
  -o OUTPUTFILE, --output_to_file OUTPUTFILE
                        Save results to the provided file name.
  -S {left,right}, --shift {left,right}
                        Choose between 'right' or 'left' direction for key
                        shift. Default = "right"
  -T {Caesar,Substitution,Vigenere}, --type {Caesar,Substitution,Vigenere}
                       Choose between encryption methods. Default = "Caesar"

```

If no arguments are specified upon running this program, the program will execute normally using the default settings. 
The default is to ask for some plaintext to encrypt via a simple Caesar cipher. 
The optional arguments shown above allow the user to select whether they wish to encrypt plaintext or decrypt some ciphertext.
Users can select one of three simple ciphers and if they want to either load data from a file or save the results to a file.

Operating System specific instructions are included below:

### Linux

If you're in the same directory as this Python's project file, simply enter the following command:

```
# If you only have Python3 installed or Python3 is set as your default
$ python cipher.py
or
$ python cipher.py -h

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 cipher.py
or
$ python3 cipher.py -h
```
If you're not in the directory where this Python's project file is, you can either navigate there, 
via: cd /Path/to/the/directory/ (substituting the appropriate directory names for your system) and
run the above command. Or you can instead run the below command from your current directory and 
just specify the path to the Python project file (.py), like so:
 
```
# If you only have Python3 installed or Python3 is set as your default
$ python /Path/to/the/directory/cipher.py
or
$ python /Path/to/the/directory/cipher.py -h

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 /Path/to/the/directory/cipher.py
or
$ python3 /Path/to/the/directory/cipher.py -h
```

### Windows

On some recent versions of Windows, it's possible to run Python scripts by only entering
the name of the file containing this project's code at the command prompt:
```
C:\> cipher.py
or
C:\> cipher.py -h
```
If you're in the same directory as this Python's project (.py) file, simply enter the above command,
or you can directly call the python interpreter via the below command: 
```
C:\> python cipher.py
or
C:\> python cipher.py -h
```
If you're not in the directory where this Python's project file is, you can either navigate there, 
via: cd /Path/to/the/directory/ (substituting the appropriate directory names for your system) and
run the above command. Or you can instead run the below command from your current directory and 
just specify the path to the Python project file (.py), like so:
```
C:\> python /Path/to/the/directory/cipher.py
or
C:\> python /Path/to/the/directory/cipher.py -h
```

### MacOS

If you're in the same directory as this Python's project file, simply enter the following command:

```
# If you only have Python3 installed or Python3 is set as your default
$ python cipher.py
or 
$ python cipher.py -h

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 cipher.py
or
$ python3 cipher.py -h
```
If you're not in the directory where this Python's project file is, you can either navigate there, 
via: cd /Path/to/the/directory/ (substituting the appropriate directory names for your system) and
run the above command. Or you can instead run the below command from your current directory and 
just specify the path to the Python project file (.py), like so:
 
```
# If you only have Python3 installed or Python3 is set as your default
$ python /Path/to/the/directory/cipher.py
or
$ python /Path/to/the/directory/cipher.py -h

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 /Path/to/the/directory/cipher.py
or
$ python3 /Path/to/the/directory/cipher.py -h
```
Upon the successful execution of this project's python (.py) file, the default execution will resemble 
something similar to the results shown below (with the values for the plaintext provided by the user and 
the subsequent ciphertext looking somewhat different depending on the option selected).

```
| ==> python3 cipher.py

	**** Default setting is to Encrypt! ****


Please enter text to encrypt
	:Some Plain text we need to keep secret.

Please enter an integer for Cipher to utilize as a key : 3

Thank You!

	**** ENCRYPTING ****


Plain text:
 Some Plain text we need to keep secret.

	**** SUCCESS! ****


Encrypted text:
 Vrph#Sodlq#whAw#zh#qhhg#wr#nhhs#vhfuhw;

```

## Author

* **Peter Robards** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


