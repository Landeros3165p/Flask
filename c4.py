network_config = {
"0001": {
 "ip": "192.168.0.2",
 "device":"switch",
 "policy":"Deny ALL",
"status": False,
"Lista":[1,4,6,0,8]

},

"0002":{
    "ip": "192.168.0.3",
     "device": "firewall",
     "policy": "avoid.2.3.4",
     "status": True
},
"0003":{
    "ip": "192.168.0.1",
     "device": "firewall",
     "policy": "avoid.2.3.4",
     "status":True
},
"0004":{
    "ip": "192.168.0.4",
     "device": "firewall",
     "policy": "avoid.2.3.4",
     "status":True
},
"0005":{
    "ip": "192.168.0.5",
     "device": "firewall",
     "policy": "avoid.2.3.4",
     "status":True
}



}
print(network_config.get("0001").get("Lista")[2])
"""
contenido = network_config.get("0001")
listaA = contenido.get('lista')
num=listaA[2]

print(num)"""