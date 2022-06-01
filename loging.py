#!/usr/bin/python3

from datetime import datetime
import os
class MyLogging(object):
    def __init__(self, log_file_path:str) -> None:
        log_file_folder, log_file_name = os.path.split(log_file_path)
        log_file_name = log_file_name.split('.')[0] + '.log'
        log_file_path = os.path.join(log_file_folder, log_file_name)
        if not (os.path.exists(log_file_path) and os.path.isfile(log_file_path)):
            log_file = open(log_file_path, 'w', encoding='utf-8')
            log_file.close()
        self.log_file_name = log_file_path
        self.text_color = {
            'light_blue':   '\033[1;34m',
            'light_yellow': '\033[1;33m',
            'light_red':    '\033[1;31m',
            'light_green':  '\033d 1;32m',
            'white':        '\033[1;37m',
            'reset_color':  '\033[0m',
        }
        self.label = {
            'successful':  ['[s]', self.text_color['light_green']],
            'information': ['[i]', self.text_color['light_blue']],
            'warning':     ['[w]', self.text_color['light_yellow']],
            'error':       ['[e]', self.text_color['light_red']],
        }
    
    def add_log(self, type_log:str, message:str) -> None:
        if type_log not in self.label.keys():
            print(
                self.label['error'][1],
                self.label['error'][0],
                self.text_color['white'],
                datetime.strftime(datetime.now(), '[%d-%m-%Y %H:%M:%S]'),
                'Sorry! I dont know this a type_log. =(',
                self.text_color['reset_color'],
            )
        else:
            log_mess_for_cli = [
                self.label[type_log][1],
                self.label[type_log][0],
                self.text_color['white'],
                datetime.strftime(datetime.now(), '[%d-%m-%Y %H:%M:%S]'),
                message
            ]
            log_mess_for_file = [log_mess_for_cli[1], log_mess_for_cli[3], log_mess_for_cli[4]]
            with open(self.log_file_name, 'a', encoding='utf-8') as f:
                f.write(' '.join(log_mess_for_file) + '\n')
            print(' '.join(log_mess_for_cli))
            

if __name__ == '__main__':
    l = MyLogging('test_log.log')
    l.add_log(type_log='successful', message='successful')
    l.add_log(type_log='information', message='information')
    l.add_log(type_log='warning', message='warning')
    l.add_log(type_log='error', message='error')
