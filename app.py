from flask import Flask, jsonify
import json

with open("API.json", "r") as json_api:
    datos_json = json.load(json_api)

app = Flask(__name__)

def find_insert(lista):
    """
    Mateo Lander Bustamante Rosales | 2026-09-21
    Modified:
        2026-09-21 | inicial version

    """
    return f"Procesado: {lista}"

@app.route('/')
def inicio():
    print('cambio')
    return datos_json("3D:RF:00:01::")

@app.route('/json/<mac>')
def json_data(mac):
    return datos_json[mac]["Name"]sf

@app.route('/server_1')
def server_1():
    find_insert(101)
    return jsonify({
        "101": {
            "Nombre": "Router Principal",
            "ip": "192.168.1.10",
            "Politica": "ALLOW_ALL",
            "Estado": "Activo"
        }
    })

@app.route('/server_2')
def server_2():
    return jsonify({
        "102": {
            "Nombre": "Router",
            "ip": "192.168.1.20",
            "Politica": "RESTRICTED",
            "Estado": "Mantenimiento"
        }
    })

@app.route('/server_3')
def server_3():
    return jsonify({
        "103": {
            "Nombre": "Switch",
            "ip": "192.168.1.30",
            "Politica": "VLAN_ONLY",
            "Estado": "Activo"
        }
    })

@app.route('/server_4')
def server_4():
    return jsonify({
        "104": {
            "Nombre": "Servidor principal",
            "ip": "192.168.1.40",
            "Politica": "STRICT_AUTH",
            "Estado": "Standby"
        }
    })

@app.route('/server_5')
def server_5():
    return jsonify({
        "105": {
            "Nombre": "Impresora",
            "ip": "192.168.1.50",
            "Politica": "LOCAL_ONLY",
            "Estado": "Inactivo"
        }
    })

@app.route('/server_6')
def server_6():
    return jsonify({
        "106": {
            "Nombre": "Firewall Perimetral",
            "ip": "192.168.1.1",
            "Politica": "BLOCK_IP",
            "Estado": "Activo"
        }
    })

@app.route('/server_7')
def server_7():
    return jsonify({
        "107": {
            "Nombre": "PC",
            "ip": "192.168.1.60",
            "Politica": "USER_DEFAULT",
            "Estado": "Activo"
        }
    })

@app.route('/server_8')
def server_8():
    return jsonify({
        "108": {
            "Nombre": "TV",
            "ip": "192.168.1.70",
            "Politica": "GUEST_ACCESS",
            "Estado": "Desconectado"
        }
    })

@app.route('/server_9')
def server_9():
    return jsonify({
        "109": {
            "Nombre": "Camara Seguridad IP",
            "ip": "192.168.1.80",
            "Politica": "STREAM_ONLY",
            "Estado": "Activo"
        }
    })

@app.route('/server_10')
def server_10():
    return jsonify({
        "110": {
            "Nombre": "Servidor Web",
            "ip": "192.168.1.90",
            "Politica": "HTTP_HTTPS_ONLY",
            "Estado": "Mantenimiento"
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)