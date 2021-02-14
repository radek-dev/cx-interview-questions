## Shopping basket by Radek

### Setup

Create your virtual environment with Python 3.8 (other Python version 
were not test) In my case, I use the below commands. I work in Linux, Ubuntu 20.10 (or other Debian based).

```bash
virtualenv <name_of_you_venv>
```

Activate your environment afterwards:

```bash
source <name_of_you_venv>/bin/activate
```

Load the packages I used (only *pytest* is required).

```bash
pip install -r <your_path>/cx-interview-questions/shopping_basket/requirement.txt
```

### Running the code
Use *pytest* to run the code in the folder **<your_path>/cx-interview-questions/shopping_basket**:

```bash
 pytest
 # or
 pytest -v
```

### Checking syntax
You can use Flake8 for syntax checking.

```bash
flake8
```