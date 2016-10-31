# Use NHTSA API to Evaluate the Safety of your Car
# NHTSA API: http://www.nhtsa.gov/webapi/Default.aspx?SafetyRatings/API/5

import requests

from json import loads


def print_result(apiUrl, apiParam, outputFormat):
    # Combine all three variables to make up the complete request URL
    response = requests.get(apiUrl + apiParam + outputFormat)
    # code below is only to handle JSON response object/format
    # use equivalent sets of commands to handle xml response object/format
    json_obj = response.json()
    # Load the Result (vehicle collection) from the JSON response
    print('------------------------------')
    print('           Result             ')
    print('------------------------------')
    for objectCollection in json_obj['Results']:
        # Loop each vehicle in the vehicles collection
        for safetyRatingAttribute, safetyRatingValue in
        objectCollection.items():
            print('{}: {}'.format(safetyRatingAttribute, safetyRatingValue))

# I. Discover available model years

apiurl = 'http://www.nhtsa.gov/webapi/api/SafetyRatings'
apiParam = ''
outputFormat = '?format=json'

print_result(apiUrl, apiParam, outputFormat)

# II. Get a list of vehicle makers for a given model year.

apiParam = '/modelyear/2013'

print_result(apiUrl, apiParam, outputFormat)

# III. Get a list of vehicle models for a given make and model year

apiParam = '/modelyear/2013/make/VOLVO'

print_result(apiUrl, apiParam, outputFormat)

# IV. Get a list of vehicle versions for a given model year, make and model

print_result(apiUrl, apiParam, outputFormat)
'''
------------------------------
           Result
------------------------------
VehicleDescription :  2013 Volvo XC90 SUV AWD
VehicleId :  7001
VehicleDescription :  2013 Volvo XC90 SUV FWD
VehicleId :  7002
'''

# V. Get Detailed Safety Data

apiParam = '/VehicleId/7002/'
print_result(apiUrl, apiParam, outputFormat)
