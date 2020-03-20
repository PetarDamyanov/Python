from datetime import datetime, timedelta
import unittest

def validate_conditions(conditions):
    counter = 0
    for condition in conditions:
        if not condition.get('hours'):
            counter += 1
        if condition.get('hours',0) > 24:
            raise ValueError('Hours cannot be > 24.')

    if counter != 1:
        raise ValueError('Invalid conditions.')

def ensure_conditions(conditions):
    # Ensure all condtions have hoursif
    # if validate_conditions(conditions)
    for condition in conditions:
        if not condition.get('hours'):
            condition.update({"hours":0})
    # if condition in conditions:
    #     if not condition.get('hours'):
    #         raise ValueError("Invalid conditions.")
    # return conditions


def group_conditions(conditions):
    # TODO
    l=[]
    for x in range(0,len(conditions)-1):
        l.append((conditions[x].get('hours'),conditions[x+1].get('hours'),conditions[x].get('percent')) )
    return l


def get_current_condition(conditions, start, now):
    h=(start-now).total_seconds()/3600
    # print(h)
    if h<=0:
        return 100
    if h>=int(conditions[0][0]):
        return int(conditions[0][2])
    for condition in conditions:
        if h<=int(condition[0]) and h>int(condition[1]):
            return int(condition[2])
        # print("{0}-{1}".format(int(condition[0]),int(condition[1])))


def get_cancellation_fee(price, percent):
    return int(price * (percent / 100))


def get_cancellation_policy(
    conditions,
    price,
    start,
    now
):
    assert start < now


def main():
    now = datetime.now()
    booking_start = now + timedelta(hours=10)
    price = 1000
    conditions = [
        {'hours': 24, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'percent': 100}
    ]
    conditions=validate_conditions(conditions)
    percent=0
    if len(conditions)>1:
        conditions=group_conditions(conditions)
        percent=get_current_condition(conditions,booking_start,now)
    else:
        percent=conditions.get('percent')
    get_cancellation_fee(price,percent)

    result = get_cancellation_policy(
        conditions,
        price,
        booking_start,
        now
    )




    print(result)


if __name__ == '__main__':
    main()