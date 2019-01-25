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

        self.granule_id = self.__checkGranuleId(granule_id)

        self.acquisition_time = self.__checkTimestamp(acquisition_time)


    def __checkGranuleId(self, granule_id):
        """
        Checks whether the value for the granule id is reasonable or not

        :param granule_id: string (formatted as Txxxxx, e.g 'T33UVP')
        """

        #
        # Check for None and length
        #
        if granule_id is None or len(granule_id) != 6:
             raise Exception('Invalid granule id {granule_id}'.format(granule_id = granule_id))
        
        #
        # Do the conversion
        #        
        granule_id_candidate = granule_id.lower()
        
        #
        # Check several values
        #                
        if granule_id_candidate[0] != 't':
            raise Exception('Invalid granule id {granule_id}. It need to start with "t", e.g. "T33UVP".'.
                format(granule_id = granule_id))
                   
        try:
            strip_number = int(granule_id_candidate[1:2])
            if strip_number > 66 or strip_number < 10:
                raise Exception()
        except Exception:
            raise Exception('Invalid granule id {granule_id}. "T" needs to be followed by exactly two digits, e.g. "T33UVP".'.
                format(granule_id = granule_id))
        
        for char in granule_id_candidate[3:6]:
            if char.isalpha() == False:
                raise Exception('Invalid granule id {granule_id}. The digits need to be followed by exactly three letters, e.g. "T33UVP".'.
                    format(granule_id = granule_id))

        #
        # Return if it passed all tests
        #
        return granule_id_candidate
    

    def __checkTimestamp(self, acquisition_time):
        """
        Checks whether the value for the acquisition time is reasonable or not

        :param acquisition_time: string (formatted as YYYYMMDDHHMMSS, e.g. '20170105T013442')
        """

        #
        # Check for None
        #
        if acquisition_time is None:
             raise Exception('Invalid acquisition_time {acquisition_time}'.
                format(acquisition_time =acquisition_time))

        #
        # Do the conversion
        #        
        acquisition_time_candidate = (parser.parse(acquisition_time)).timetuple()

        #
        # Check several values
        #          
        if acquisition_time_candidate.tm_year < 2015:
            raise Exception('Invalid year {year} in acquisition time {acquisition_time}'.
                format(year = acquisition_time_candidate.tm_year, acquisition_time =acquisition_time))

        #
        # Return if it passed all tests
        #
        return acquisition_time_candidate


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