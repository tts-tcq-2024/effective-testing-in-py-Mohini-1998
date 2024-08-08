from unittest.mock import patch
alert_failure_count = 0
counter=0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
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
        global alert_failure_count
        alert_failure_count += 0

@patch("builtins.print")
def fake_print_alert(celcius,mock_print):
    network_alert_stub(celcius)
    mock_print.assert_called_with('ALERT: Temperature is '+str(celcius)+' celcius')

alert_in_celcius(400.5)
alert_in_celcius(303.6)
alert_in_celcius(20)
fake_print_alert(30)

assert (alert_failure_count==1)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
