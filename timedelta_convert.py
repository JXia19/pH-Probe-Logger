# Author: Jing Xia
# Date: August 23rd, 2022
# Version: 1.0
# This program is used in pH PROBE LOG ONLY
# It converts timedelta result into the reporting format

def timedelta_convert(timedelta_format, probe_number):
    total_time = str(timedelta_format)
    total_time_frags = total_time.split("days",)
    hr_min_sec = total_time_frags[1].split(":",)
    total_time_frags.pop()
    total_time_frags.extend(hr_min_sec)
    usage_report_text = "Probe " + str(probe_number) + " has been in use for " + total_time_frags[0] + "days" \
                        + total_time_frags[1] + " hours " + total_time_frags[2] + " minutes and " + \
                        total_time_frags[3] + " seconds.\n"

    return(usage_report_text)
