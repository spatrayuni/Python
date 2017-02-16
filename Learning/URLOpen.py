from urllib2 import urlopen

PAGE = 'https://cloudacademy.com'
TEXT = 'AWS'

def lambda_handler(event, context):
    print('Event: %s' % event)
    t = event.get('time') or "?"
    if TEXT in urlopen(PAGE).read():
        print('Found!')
        return "OK @ %s" % t
    else:
        print('Not Found!')
        raise Exception('%s not found in %s @ %s' % (TEXT, PAGE, t))


        {
    "account": "XXX",
    "region": "us-west-2",
    "detail": {},
    "detail-type": "Scheduled Event",
    "source": "aws.events",
    "time": "2016-10-25T00:00:00Z",
    "id": "cdc73f9d-aea9-11e3-9d5a-835b769c0d9c",
    "resources": [
        "arn:aws:events:us-east-1:123456789012:rule/MonitorWebsiteTask"
    ]
}