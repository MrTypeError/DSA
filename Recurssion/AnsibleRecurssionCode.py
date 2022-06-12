from copy import deepcopy
config=dict(
            access_group=dict(
                peer=[
                    dict(access_list="2", kod=True),
                    dict(
                        access_list="preauth_ipv6_acl",
                        ipv6=True,
                        kod=True,
                    ),
                ]
            ),
            allow=dict(control=dict(rate_limit=4)),
            authenticate=True,
            authentication_keys=[
                dict(
                    algorithm="md5",
                    encryption=7,
                    id=2,
                    key="SomeSecurePassword",
                )
            ],
            broadcast_delay=22,
            logging=True,
            master=dict(stratum=4),
            max_associations=34,
            max_distance=3,
            min_distance=10,
            orphan=4,
            panic_update=True,
            peers=[
                dict(peer="172.16.1.10", version=2),
                dict(
                    key_id=2,
                    minpoll=5,
                    peer="172.16.1.11",
                    prefer=True,
                    version=2,
                ),
                dict(
                    peer="checkPeerDomainIpv4.com",
                    prefer=True,
                    use_ipv4=True,
                ),
                dict(peer="checkPeerDomainIpv6.com", use_ipv6=True),
                dict(
                    peer="testPeerDomainIpv6.com",
                    prefer=True,
                    use_ipv6=True,
                ),
            ],
            servers=[
                dict(server="172.16.1.12", version=2),
                dict(
                    server="172.16.1.13", source="GigabitEthernet0/1"
                ),
                dict(
                    server="checkServerDomainIpv6.com", use_ipv6=True
                ),
            ],
            source="GigabitEthernet0/1",
            trusted_keys=[
                dict(range_start=21),
                dict(range_end=13, range_start=3),
            ],
            update_calendar=True,
        ),

def _ntp_list_to_dict(data):
    """Convert all list of dicts to dicts of dicts"""
    p_key = {
        "servers": "server",
        "peers": "peer",
        "authentication_keys": "id",
        "peer": "access_list",
        "query_only": "access_list",
        "serve": "access_list",
        "serve_only": "access_list",
        "trusted_keys": "range_start",
        "access_group": True,
    }
    tmp_data = deepcopy(data)
    for k, _v in p_key.items():
        if k in tmp_data and k != "access_group":
            if k in ["servers", "peers"]:
                for i in tmp_data[k]:
                    if i.get("key"):
                        del i["key"]
            tmp_data[k] = {str(i[p_key[k]]): i for i in tmp_data[k]}
        elif tmp_data.get("access_group") and k == "access_group":
            tmp_data[k] =_ntp_list_to_dict(
                tmp_data.get("access_group")
            )
    return tmp_data

Newdata=_ntp_list_to_dict(data)
print