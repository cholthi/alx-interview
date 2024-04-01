#!/usr/bin/env python3
""" Parses logs from stdin and outputs useful data from it"""
import re


def get_chunk(n_lines):
    """Returns interator that emits 10 lines from 
    the file object at a time. """
    chuck = []
    line_no = 0
    while True:
        line = input()
        line_no += 1
        if not line:
            raise StopIteration

        chuck.append(str(line))
        if line_no % n_lines == 0:
            yield chuck

def extract_data(chuck):
    """extract data from the lines in chuck"""
    data_stats = []
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    format_str = '{}\\-{}{}{}{}\\s*'.format(
            fp[0], fp[1], fp[2], fp[3], fp[4])
    for line in chuck:
        match = re.search(format_str, line)
        if match:
            data_stats.append(match.groupdict())
    return data_stats



def process_chunk(chuck, status_codes, total_file_size):
    """ processes 10 lines of a file at a time"""
    if chuck is None:
        print_chuck(total_file_size, status_codes)
        return -1
    stats = extract_data(chuck)
    total_file_size += compute_stats(stats, status_codes, total_file_size)
    print_chuck(total_file_size, status_codes)
    return total_file_size


def print_chuck(size, status_codes):
    """prints stats in a chuck"""
    print('File size: {:d}'.format(size), flush=True)
    for status_code in sorted(status_codes.keys()):
        feq = status_codes.get(status_code, 0)
        if feq > 0:
            print('{:s}: {:d}'.format(status_code, feq), flush=True)

def compute_stats(stats, status_codes, file_size):
    """Compute the printable final stats from list of raw stats"""
    #file_size = 0
    for stat in stats:
        status = stat.get('status_code', 0)
        if status in status_codes:
            status_codes[status] += 1
        file_size += int(stat.get('file_size'))
    return file_size





if __name__ == '__main__':
   
    file_size = 0
    status_codes = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0,
        }
    
    try:
        for chunk in get_chunk(10):
            file_size += process_chunk(chunk, status_codes, file_size)
    except (KeyboardInterrupt, EOFError):
        process_chunk(None, status_codes, file_size)
