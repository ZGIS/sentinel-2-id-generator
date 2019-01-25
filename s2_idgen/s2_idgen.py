from datetime import datetime
from dateutil import parser
import math

class Generator:

    def __init__(self, granule_id, acquisition_time):
        """
        Constructor
        :param granule_id: string (formatted as Txxxxx, e.g 'T33UVP')
        :param acquisition_time: string (formatted as YYYYMMDDHHMMSS, e.g. '20170105T013442')
        """
        #
        # User lowercase of
        #
        self.granule_id = granule_id.lower()
        self.acquisition_time = (parser.parse(acquisition_time)).timetuple()
        
        #TODO: Check and sanitize inputs
        
    def getID(self):
        """
        getId.
        return: string (formatted as {granule-id}-{acquisitionyear}-{acquisitiondayofyear}-{acquisitionhour}-{acquisitiontime as (minutes / 5)})
        """
        acquisitionyear = self.acquisition_time.tm_year
        acquisitiondayofyear = self.acquisition_time.tm_yday
        acquisitionhour = self.acquisition_time.tm_hour
        acquisitiontime = math.floor(self.acquisition_time.tm_min / 5)
        
        return '{granule_id}-{acquisitionyear}-{acquisitiondayofyear}-{acquisitionhour}-{acquisitiontime}'.format(
                        granule_id = self.granule_id,
                        acquisitionyear = acquisitionyear,
                        acquisitiondayofyear = '{0:03d}'.format(acquisitiondayofyear),
                        acquisitionhour = '{0:02d}'.format(acquisitionhour),
                        acquisitiontime = acquisitiontime
                    )