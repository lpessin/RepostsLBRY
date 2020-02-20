import requests

def get_all_claims_reposts():
    id_list = []
    claims = []
    call = requests.post("http://localhost:5279", json={"method": "claim_list", "params": {"page_size": 99999}}).json()
    result = call['result']['items']
    for claim in result:
        ids = claim['claim_id']
        id_list.append(ids)
    for id in id_list:
        call = requests.post("http://localhost:5279", json={"method": "claim_search",
                                                            "params": {'claim_id': id,
                                                                       "page_size": 99999}}).json()
        result = call['result']['items']
        for claim in result:
            if claim['value_type'] != 'repost':
                name = claim['name']
                rep = claim['meta']['reposted']
                claims.append([name, rep])
    return [claims]

def get_reposts_by_channel(channel):
    claims = []
    call = requests.post("http://localhost:5279", json={"method": "claim_search",
                                                        "params": {'channel': channel,
                                                                   "page_size": 99999}}).json()
    result = call['result']['items']
    for claim in result:
        if claim['value_type'] != 'repost':
            name = claim['name']
            rep = claim['meta']['reposted']
            claims.append([name, rep])
    return [claims]

def printChannel(channel):
    print(10 * '=', 'Posts Reposted', 10 * '=')
    get = get_reposts_by_channel(channel)
    n = 0
    n1 = 0
    n2 = 0
    for i in get:
        for b in i:
            r = int(b[1])
            n2 = n2 + r

            if r >= 1:
                print(f'{b[0]}: {b[1]} Reposts')
                n += 1
            else:
                n1 += 1

    print(20 * '=')
    print(f'Posts Reposted: {n}\nTotal Reposts: {n2}')
    print(20 * '=')

def printAll():
    print(10 * '=', 'Posts Reposted', 10 * '=')
    get = get_all_claims_reposts()
    n = 0
    n1 = 0
    n2 = 0
    for i in get:
        for b in i:
            r = int(b[1])
            n2 = n2 + r

            if r >= 1:
                print(f'{b[0]}: {b[1]} Reposts')
                n += 1
            else:
                n1 += 1

    print(20 * '=')
    print(f'Posts Reposted: {n}\nTotal Reposts: {n2}')
    print(20 * '=')

# printAll()
printChannel('@youtubekiller')
