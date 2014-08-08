import time
import re

from logster.logster_helper import MetricObject, LogsterParser
from logster.logster_helper import LogsterParsingException

class NginxLog(LogsterParser):

    def __init__(self, option_string=None):
        '''Initialize any data structures or variables needed for keeping track
        of the tasty bits we find in the log we are parsing.'''
        self.http_code = {
            'http_1xx': 0,
            'http_2xx': 0,
            'http_3xx': 0,
            'http_4xx': 0,
            'http_5xx': 0,
        }


        # Regular expression for matching lines we are interested in, and capturing
        # fields from the line (in this case, http_status_code).
        self.reg = re.compile('.*HTTP/1.\d\" (?P<http_status_code>\d{3}) .*')


    def parse_line(self, line):
        '''This function should digest the contents of one line at a time, updating
        object's state variables. Takes a single argument, the line to be parsed.'''

        try:
            # Apply regular expression to each line and extract interesting bits.
            regMatch = self.reg.match(line)

            if regMatch:
                linebits = regMatch.groupdict()
                status = int(linebits['http_status_code'])

                if (status < 200):
                    self.http_code['http_1xx'] += 1
                elif (status < 300):
                    self.http_code['http_2xx'] += 1
                elif (status < 400):
                    self.http_code['http_3xx'] += 1
                elif (status < 500):
                    self.http_code['http_4xx'] += 1
                else:
                    self.http_code['http_5xx'] += 1

            else:
                raise LogsterParsingException, "regmatch failed to match"

        except Exception, e:
            raise LogsterParsingException, "regmatch or contents failed with %s" % e

    def get_state(self, duration):
        '''Run any necessary calculations on the data collected from the logs
        and return a list of metric objects.'''
        self.duration = duration


        # Return a list of metrics objects
        return [
            MetricObject("http_1xx", self.http_code['http_1xx'], "Responses last 5 minutes"),
            MetricObject("http_2xx", self.http_code['http_2xx'], "Responses last 5 minutes"),
            MetricObject("http_3xx", self.http_code['http_3xx'], "Responses last 5 minutes"),
            MetricObject("http_4xx", self.http_code['http_4xx'], "Responses last 5 minutes"),
            MetricObject("http_5xx", self.http_code['http_5xx'], "Responses last 5 minutes"),
        ]

