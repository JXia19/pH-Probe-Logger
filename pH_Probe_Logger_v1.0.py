# Author: Jing Xia
# Date: August 11th, 2022
# Version: 1.0
# This program is used to simplify logging process
# for Fermentation Team
# PH PROBE LOG ONLY

import sys
import PySimpleGUI as sg

from probe_usage import *
from log_usage import *
from self_check import *


#File path need to be updated depending on location and device
## Will add an argument reader later on
file_path = 'pH_Probe_Log.xlsx'

continue_program = True


while continue_program == True:

    #Performs error check, system will force exit if there's been an error in previous logs
    error = error_log_check(file_path)
    if error == True:
        sys.exit()
    probe_life_check(file_path)

    
    function_option_layout = [[sg.Text("What function are you looking to perform?")], \
                               [sg.Button("Check Current Probe Time")], \
                               [sg.Button("Log Probe Use")],[sg.Cancel()]]
    
    function_option_window = sg.Window("Choose your function", function_option_layout)
    function_option_event, function_option_values = function_option_window.read()
    function_option_window.close()

    
    if function_option_event == "Check Current Probe Time":
        probe_usage(file_path)
        continue_program = True

    elif function_option_event == "Log Probe Use":
        log_usage(file_path)
        continue_program = True

    elif function_option_event == 'Cancel' or function_option_event == sg.WIN_CLOSED:
        sys.exit()
        continue_program = False
