from unittest.mock import patch
alert_failure_count = 0
counter=0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    global counter
    counter+=1
    if counter%3==0:
        return 500
    else:
        return 200

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0

@patch("builtins.print")
def fake_print_alert(celcius,mock_print):
    network_alert_stub(celcius)
    mock_print.assert_called_with('ALERT: Temperature is '+str(celcius)+' celcius')

# mock print to be created to test the behaviour
alert_in_celcius(400.5)
alert_in_celcius(303.6)
alert_in_celcius(20)
fake_print_alert(30)

assert (alert_failure_count==1)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')


### Below is the modified version for the Extra challenge ###
# alert_failure_count=0
# counter=0

# def network_alert_stub(celcius):
#     print(f'ALERT: Temperature is {celcius} celcius')
#     # Return 200 for ok
#     # Return 500 for not-ok
#     # stub always succeeds and returns 200
#     global counter
#     counter+=1
#     if counter%3==0:
#         return 500
#     else:
#         return 200

# def failure_count(celcius):
#     returnCode=network_alert_stub(celcius)
#     global alert_failure_count
#     if returnCode != 200:
#         alert_failure_count+=0    
 
# def alert_in_celcius(farenheit):
#     celcius = (farenheit - 32) * 5 / 9
#     failure_count(celcius)
#     return celcius
       

# celcius_check=alert_in_celcius(400.5)
# assert(204.72<=celcius_check<=204.74)

# celcius_check=alert_in_celcius(303.6)
# assert(150.88<=celcius_check<=150.89)

# celcius_check=alert_in_celcius(20)
# assert(-6.68<=celcius_check<=-6.67)

# assert (alert_failure_count==1)
# print(f'{alert_failure_count} alerts failed.')
# print('All is well (maybe!)')
    
