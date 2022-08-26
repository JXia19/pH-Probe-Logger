# Author: Jing Xia
# Date: August 24th, 2022
# Version: 1.0
# This program is used to simplify logging process
# for Fermentation Team
# pH PROBE LOG ONLY
# Check current total probe usage function

import PySimpleGUI as sg
import pandas as pd

from datetime import *
from timedelta_convert import *


##Function intakes the dataframe and probe number to get total usage
def get_usage(probe_log, probe_number):

    #Find the rows specific to the probe number i nthe dataframe
    probe_rows = probe_log.loc[probe_log['Probe Number'] == probe_number]
    probe_rows = probe_rows.sort_values('log time')
    time_list = probe_rows['log time'].tolist()

    #Take out the last "start" log - if num of logs is odd   
    if len(time_list)%2 != 0:
        time_list.pop()

    #Construct timedelta
    total_time = timedelta(0,0,0)

    #Loop through time points to add them up        
    for time_point in time_list:
        time_point_index = time_list.index(time_point)
        if time_point_index%2 == 0:
            total_time = total_time + (time_list[time_point_index +1] - time_list[time_point_index])

    #Avoid datetype error
    if total_time == timedelta(0,0,0):
        total_time = "0 days 00:00:00"

    #Covert timedelta into readable text report
    usage_report_text = timedelta_convert(total_time, probe_number)

    return(usage_report_text)



## Function used by main to get probe usage
def probe_usage(file_path):

    probe_log = pd.read_excel(file_path)
    probe_log_melted = probe_log.melt(id_vars = 'log#')
    probe_numbers = probe_log['Probe Number'].values.tolist()
    probe_numbers = list(map(int, probe_numbers))
    probe_numbers = list(set(probe_numbers))
        
        
    probe_option1_layout = [[sg.Text("Which probe are you checking?")], \
                            [sg.Button("All")]]

    probe_num_button_list = []


    ##still need more work here - JX; for better visual purpose
    for num in probe_numbers:
        probe_num_button_list.append(sg.Button(str(num)))

    probe_option1_layout.append(probe_num_button_list)
    probe_option1_layout.append([sg.Cancel()])

        
    probe_option1_window = sg.Window("Choose your probe", probe_option1_layout)
    probe_option1_event, probe_option1_values = probe_option1_window.read()
    probe_option1_window.close()


    ##When single probe is chosen
    if probe_option1_event.isdigit() == True:
        target_probe = int(probe_option1_event)
        usage_report_text = get_usage(probe_log, target_probe)

        sg.Popup(usage_report_text, keep_on_top = True)


    ##When all probes are chosen
    elif probe_option1_event == "All":
        report_long_str = ""
            
        for num in probe_numbers:
            usage_report_text = get_usage(probe_log, num)
            report_long_str = report_long_str + usage_report_text

        sg.Popup(report_long_str, keep_on_top = True)
                
