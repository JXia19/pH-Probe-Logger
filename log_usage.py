# Author: Jing Xia
# Date: August 24th, 2022
# Version: 1.0
# This program is used to simplify logging process
# for Fermentation Team
# pH PROBE LOG ONLY
# Performs user pH probe usage logging function

import PySimpleGUI as sg

import pandas as pd
from openpyxl import load_workbook

from datetime import *

def log_usage(file_path):
    probe_log = pd.read_excel(file_path)
    probe_log_melted = probe_log.melt(id_vars = 'log#')
    probe_numbers = probe_log['Probe Number'].values.tolist()
    probe_numbers = list(map(int, probe_numbers))
    probe_numbers = list(set(probe_numbers))
    
    exp_numbers = probe_log['Exp#'].values.tolist()
    for item in exp_numbers:
        if item == 'Cal':
            exp_numbers.remove(item)
            
    exp_numbers = list(map(int,exp_numbers))
    last_exp_numbers = exp_numbers[-4::1]
    last_exp_numbers = list(set(last_exp_numbers))
    last_exp_numbers.append('Cal')

    now = datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    

    values_list = []
    loop = True

    while loop == True:
        log_layout = [[sg.Text("Log Usage:")],[sg.Text("Operator:"),sg.Combo(["AO","EW","ML","SD","NR","ET","JX"], \
                        default_value = "AO",readonly=True,key = "operator")],\
                      [sg.Text("Probe Number:"),sg.Combo(probe_numbers,key="prob_num")],\
                      [sg.Text("Start log or end log:"), sg.Combo(["start","end"], default_value = "start",\
                        readonly=True,key = "start_end")],\
                      [sg.Text("Experiment Number (use 'Cal' for calibration):"), sg.Combo(last_exp_numbers, default_value = last_exp_numbers[0],\
                        key = "exp_num")],
                      [sg.Text("Time Log:"),sg.Combo(values_list,default_value=now,\
                        size=(20,1),key="time")],[sg.Button("Save"),sg.Cancel()]]
        
        log_window = sg.Window("Enter log info", log_layout)
                       
        log_e, log_v = log_window.read()
        log_window.close()

        if log_e == "Save":
            exp_num = int(log_v['exp_num'])
            operator = log_v['operator']
            time = datetime.strptime(log_v['time'],"%Y-%m-%d %H:%M:%S")
            start_end = log_v['start_end']
            next_entry_row = len(probe_log.index)+1

            if log_v['prob_num'] is None:
                sg.Popup("Entry for probe number cannot be empty! Please re-enter your log.")
                loop == True

            elif str(log_v['prob_num']).isdigit() == False:
                sg.Popup ("Entery for probe number has to be a integer! Please re-enter your log.")
                loop == True
            
            else:
                prob_num = int(log_v['prob_num'])
                entry = [next_entry_row, exp_num, operator,time,start_end,prob_num]
            
                #log_df = pd.DataFrame(entry)
                wb = load_workbook(file_path)
                ws = wb.worksheets[0]
                ws.append(entry)
                wb.save(file_path)
                loop = False

        elif log_e == "Cancel" or log_e == sg.WIN_CLOSED():
            loop = False
