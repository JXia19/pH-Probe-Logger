# Author: Jing Xia
# Date: August 25th, 2022
# Version: 1.0
# This program is used to simplify logging process
# for Fermentation Team
# pH PROBE LOG ONLY
## Performs self check functions

import sys
import PySimpleGUI as sg
import pandas as pd

def error_log_check(file_path):
    probe_log = pd.read_excel(file_path)
    probe_log_melted = probe_log.melt(id_vars = 'log#')
    probe_numbers = probe_log['Probe Number'].values.tolist()
    probe_numbers = list(map(int, probe_numbers))
    probe_numbers = list(set(probe_numbers))

    for num in probe_numbers:
        probe_rows = probe_log.loc[probe_log['Probe Number'] == num]
        probe_rows = probe_rows.sort_values('log time')

        start_end_list = probe_rows['start or end'].tolist()
        log_num_list = probe_rows['log#'].tolist()
        log_num_to_state = dict(zip(log_num_list, start_end_list))

        counter = 0
        error = False
        for key in log_num_to_state:
            counter = counter + 1
            if (counter %2 != 0) and (log_num_to_state[key] != 'start'):
                start_error_text = "There's been an entry error for log #" + str(key) + "\nPlease fix the error manually. \nProgram has ended."
                sg.Popup(start_error_text, keep_on_top = True)
                error = True
                return(error)
            elif (counter %2 == 0) and (log_num_to_state[key] != 'end'):
                end_error_text = "There's been an entry error for log #" + str(key) + "\nPlease fix the rror manually. \nProgram has ended."
                sg.Popup(end_error_text, keep_on_top = True)
                error = True
                return(error)
                         
def probe_life_check(file_path):
    probe_log = pd.read_excel(file_path)
    probe_log_melted = probe_log.melt(id_vars = 'log#')
    probe_numbers = probe_log['Probe Number'].values.tolist()
    probe_numbers = list(map(int, probe_numbers))
    probe_numbers = list(set(probe_numbers))

    for num in probe_numbers:
        probe_rows = probe_log.loc[probe_log['Probe Number'] == num]
        exp_num_list = probe_rows['Exp#'].tolist()

        for item in exp_num_list:
            if item == "Cal":
                exp_num_list.remove(item)
                
        exp_num_list = list(map(int,exp_num_list))
        exp_num_list = list(set(exp_num_list))

        if len(exp_num_list) >= 100:
            overusage_text = "Probe has been autoclaved " + str(len(exp_num_list)) + " times."
            sg.Popup(overusage_text, keep_on_top = True)

            
