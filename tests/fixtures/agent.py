MEMBERS_RESPONSE = {
    "ServerName": "nomad02",
    "ServerRegion": "global",
    "ServerDC": "nomad",
    "Members": [
        {
            "Name": "nomad02.global",
            "Addr": "0.0.0.0",
            "Port": 4648,
            "Tags": {
                "port": "4647",
                "region": "global",
                "dc": "nomad",
                "vsn": "1",
                "build": "1.2.6",
                "id": "91a9bba0-c47d-a8fc-95a2-3cde04228379",
                "role": "nomad",
                "rpc_addr": "0.0.0.0",
                "raft_vsn": "2",
                "mvn": "1",
                "expect": "3"
            },
            "Status": "alive",
            "ProtocolMin": 1,
            "ProtocolMax": 5,
            "ProtocolCur": 2,
            "DelegateMin": 2,
            "DelegateMax": 5,
            "DelegateCur": 4
        },
        {
            "Name": "nomad01.global",
            "Addr": "0.0.0.0",
            "Port": 4648,
            "Tags": {
                "region": "global",
                "raft_vsn": "2",
                "port": "4647",
                "expect": "3",
                "vsn": "1",
                "mvn": "1",
                "dc": "nomad",
                "build": "1.2.6",
                "id": "4888ccdb-2362-a53a-c3c5-d1000c8b0e33",
                "rpc_addr": "0.0.0.0",
                "role": "nomad"
            },
            "Status": "alive",
            "ProtocolMin": 1,
            "ProtocolMax": 5,
            "ProtocolCur": 2,
            "DelegateMin": 2,
            "DelegateMax": 5,
            "DelegateCur": 4
        },
        {
            "Name": "nomad03.global",
            "Addr": "0.0.0.0",
            "Port": 4648,
            "Tags": {
                "dc": "nomad",
                "region": "global",
                "raft_vsn": "2",
                "build": "1.2.6",
                "id": "0eebebff-0814-c0c2-3e6c-84e40983fc21",
                "role": "nomad",
                "vsn": "1",
                "mvn": "1",
                "rpc_addr": "0.0.0.0",
                "port": "4647",
                "expect": "3"
            },
            "Status": "alive",
            "ProtocolMin": 1,
            "ProtocolMax": 5,
            "ProtocolCur": 2,
            "DelegateMin": 2,
            "DelegateMax": 5,
            "DelegateCur": 4
        }
    ]
}

MEMBER_NULL_TAGS = {
    "Name": "nomad02.global",
    "Addr": None,
    "Port": 4648,
    "Tags": None,
    "Status": "alive",
    "ProtocolMin": 1,
    "ProtocolMax": 5,
    "ProtocolCur": 2,
    "DelegateMin": 2,
    "DelegateMax": 5,
    "DelegateCur": 4
}
