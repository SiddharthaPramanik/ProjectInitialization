# Create.py
* Logs into Github using credentials in the script 
* Creates a new repository using the given name (& discription) in the CLI
* Makes changes on local machine, like initializing empty git

# createproject.sh
This is used to invoke the python script once sourced.

## Installation
Execute the following commands :

```
git clone "https://github.com/SiddharthaPramanik/ProjectInitialization.git"
```

```
cd ProjectInitialization
```

```
pip install -r requirements.txt
```

```
source .createproject.sh 
```
Once done successfully, 
* update createproject.sh with absolute/ relative path to create.py
* go in Create.py and update app_path, username, password variables
* update your username inplace of <Github username> in create() function

## Usage
```
create <project name> <description>
```
Examples:
```
create NewProject
```

```
create NewProject 'A new project'
```