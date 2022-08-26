# pH_Probe_Logger Requirements
 * Python 3.10

## General Info
1. timedelta_covert.py contain function that coverts reported timedelta into a readable text
2. probe_usage.py contain function that returns current total usage on all or specified probes
3. log_usage.py contain function that allows user to enter probe usage
4. self_check.py contain function that checks for entry error and overusage
5. pH_Probe_Logger_v1.0.py is the main driver; it queries the function options (GUI) and calls self check; 
   The overall program logs pH probe usage and warns for maintainance time. This helps simplifies the process
   of manual logging.

### Installation CMD Commands
pip - package installer:		"python get-pip.py"
openpyxl - read/write Excel:		"pip install openpyxl"
pandas - data manipulation:		"pip install pandas"
PySimpleGUI - GUI interface:		"pip install PySimpleGUI"
PyInstaller - bundles application:	"pip install PyInstaller"


#### Create Executable
CMD Command: "python -m PyInstaller pH_Probe_Logger_v1.0.py"
FermProbLog_v1.0.exe can be found in DIST folder

