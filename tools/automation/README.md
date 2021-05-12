# BOS Automation Tools
...

## Installation

### Pre-requisites

```
python3 -m pip install -r requirements.txt
```

## Excel sheet template

[`test/test_sheet.xlsx`](test/test_sheet.xlsx)

## Convert an Excel spreadsheet to a UDMI site model

```
./xls2udmi.py -h
      _     ____  _   _ ____  __  __ ___
__  _| |___|___ \| | | |  _ \|  \/  |_ _|
\ \/ / / __| __) | | | | | | | |\/| || |
 >  <| \__ \/ __/| |_| | |_| | |  | || |
/_/\_\_|___/_____|\___/|____/|_|  |_|___|


usage: xls2udmi.py [-h] [-v] [-d] [-i INPUT] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase the verbosity level
  -d, --debug           print debug information
  -i INPUT, --input INPUT
                        input Excel sheet file name
  -o OUTPUT, --output OUTPUT
                        output folder name
```

## Convert an Excel spreadsheet to a DBO building config file

```
./xls2dbo.py -h
      _     ____  ____  ____   ___
__  _| |___|___ \|  _ \| __ ) / _ \
\ \/ / / __| __) | | | |  _ \| | | |
 >  <| \__ \/ __/| |_| | |_) | |_| |
/_/\_\_|___/_____|____/|____/ \___/


usage: xls2dbo.py [-h] [-v] [-d] [-i INPUT]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase the verbosity level
  -d, --debug           print debug information
  -i INPUT, --input INPUT
                        input Excel sheet file name
```

## Reference

* [UDMI](https://github.com/faucetsdn/udmi)
* [UDMI site model](https://github.com/faucetsdn/udmi_site_model)
* [Digital Buildings Ontology](https://github.com/google/digitalbuildings)
