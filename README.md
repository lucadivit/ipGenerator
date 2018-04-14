# ipGenerator

A simple script written in python that generate a set of reachable IPv4.

## Installing

```
git clone https://github.com/lucadivit/ipGenerator

cd ipGeneretor

pip install -r requirements.txt
```

## Usage

Example of usage:

First example:

```
python ipGenerator.py
```

Second example:
```
python ipGenerator.py --verbose=1 --output=ipList.txt --desiredIP=2
```

For help type:
_____________

```
python ipGenerator.py --help
```

### Flags

There are some flags. Now i explain it:

```
--verbose=X where X is a number in (0,1).
```

The verbose flag provides additional details during the process.
The default value of verbose is 0 (disabled).

```
--desiredIP=Y where Y is an integer in (0,N).
```

The desiredIP flag specifies the number of reachable IP that you want in output.
The default value of desiredIP is 3.

```
--output=<file_name>.txt 
```

The output flag provides a list of reachable IP in a text file.
The default value is "" (disabled).

```
--help 
```

The help flag prints the help message.

### Output example

```
IP: 123.123.123.123 Hostname: string.of.hostname
```

## External Code

* [Progress](https://github.com/verigak/progress/) - Used for spinner


