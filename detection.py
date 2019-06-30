import conf, json, time, math, statistics
from boltiot import Sms, Bolt, Email


def compute_bounds(history_data,frame_size,factor):
    if len(history_data)<frame_size :
        return None

    if len(history_data)>frame_size :
        del history_data[0:len(history_data)-frame_size]
    Mn=statistics.mean(history_data)
    Variance=0
    for data in history_data :
        Variance += math.pow((data-Mn),2)
    Zn = factor * math.sqrt(Variance / frame_size)
    High_Bound = history_data[frame_size-1]+Zn
    print ("High bound = ", High_Bound)
    Low_Bound = history_data[frame_size-1]-Zn
    print ("Low bound = ", Low_Bound)
    return [High_Bound,Low_Bound]

mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SSID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
mailer = Email(conf.MAILGUN_API_KEY, conf.SANDBOX_URL, conf.SENDER_EMAIL, conf.RECIPIENT_EMAIL)
history_data=[]

while True:
    response = mybolt.analogRead('A0')
    response1 = mybolt.analogRead('A0')

    data = json.loads(response)

    sensor_value1 = int(data['value'])
    sensor_value1 = int((sensor_value1/10.24)*9/5 + 32)
    print ("The current temp is "+ str(sensor_value1)+" degrees F, and the sensor value is "+data['value'])
    sensor_value=0
    try:
        sensor_value = int(data['value'])
    except e:
        print("There was an error while parsing the response: ",e)
        continue

    bound = compute_bounds(history_data,conf.FRAME_SIZE,conf.MUL_FACTOR)
    if not bound:
        required_data_count=conf.FRAME_SIZE-len(history_data)
        print("I will collect ", required_data_count, " more data point(s) before I begin.")
        history_data.append(int(data['value']))
        time.sleep(5)
        continue

    try:
        if sensor_value > bound[0] :
            sensor_value1 = int((sensor_value/10.24)*9/5 + 32)
            print ("The temp  has INCREASED. Sending SMS & email.")
            response = sms.send_sms("Temp has increased. The current temperature is " + str(sensor_value1)+ " degrees F.")
            response1 = mailer.send_email("Alert", "Temp has increased. The current temperature is " + str(sensor_value1)+" degrees F.")
            print("This is the response for SMS ",response)
            print("This is the response for EMAIL ",response1)
        history_data.append(sensor_value);
    except Exception as e:
        print ("Error",e)
    time.sleep(50)

    try:
        if sensor_value < bound[1] :
            sensor_value1 = int((sensor_value/10.24)*9/5 + 32)
            print ("The temp  has decreased. Sending SMS & email.")
            response = sms.send_sms("Temp has decreased. The current temperature is " + str(sensor_value1)+ " degrees F.")
            response1 = mailer.send_email("Alert", "Temp has decreased. The current temperature is " + str(sensor_value1)+" degrees F.")
            print("This is the response for SMS ",response)
            print("This is the response for EMAIL ",response1)
        history_data.append(sensor_value);

    except Exception as e:
        print ("Error",e)
    time.sleep(50)
