import datetime

def timedelta_count(datetime1, datetime2, timestep=datetime.timedelta(hours=1), timelimit=datetime.timedelta(days=1)):
    assert datetime1 < datetime2
    count = 0
    while timestep * count <= timelimit:
        if (datetime2 - datetime1) < (timestep * count):
            return count
        count += 1
    else:
        raise RuntimeError("timedelta > timelimit. Reset timelimit.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('pong_text', help='')
    args = parser.parse_args()
    
    with open(args.pong_text, 'r') as f:
        pong_list = [dict(datetime=datetime.datetime.fromisoformat(l.split(': ')[0]), ping=''.join(l.split(": ")[1:])) for l in f.readlines()]
    
    print(len(pong_list))
    print(pong_list[0])

    datetime_list = [pong['datetime'] for pong in pong_list]

    disconnect_list = list()
    for t1, t2 in zip(datetime_list, datetime_list[1:]):
        timedelta = t2 - t1
        if timedelta > datetime.timedelta(seconds=2):
            disconnect_list.append(dict(datetime=t1, timedelta=timedelta))
            print(disconnect_list[-1])

    timedelta_count_list = list()
    for d1, d2 in zip(disconnect_list, disconnect_list[1:]):
        timedelta_count_list.append(timedelta_count(d1['datetime'], d2['datetime'], timestep=datetime.timedelta(minutes=15)))
    for i in range(24*4):
        print("{:05.2f}: {:02d}".format(i/4, timedelta_count_list.count(i)))
