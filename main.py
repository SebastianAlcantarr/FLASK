from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)
app.run(debug=True)

data={
    "cars":[
        {
            "img":'https://media.es.wired.com/photos/6579d70164ac50d8bb9309b9/16:9/w_2560%2Cc_limit/teslay-biz-GettyImages-1240065676.jpg',
            "Name" : 'Carro Testa Model S',
            "Price":'2,3000,4000 $mxn'
        },

        {
            "img":"https://hips.hearstapps.com/hmg-prod/images/ferrari-f80-67110fa962e1d.jpg?crop=1.00xw:1.00xh;0,0",
            "Name" : 'Ferrari Model F80',
            "Price":'1.000.000 $'
        },
        {
            "img":"https://i0.wp.com/indycaraldia.com/wp-content/uploads/2024/02/Huayra-R-Evo-02-3-4-Frontale.jpg?fit=1024%2C576&ssl=1",
            "Name" : 'Huayra Model R',
            "Price":'3.200.400 $'
        },
        {
            "img":"https://th.bing.com/th/id/OIP.BQ8nJo_lRPiUVp9UBuV4GgHaEi?rs=1&pid=ImgDetMain",
            "Name" : 'Bugatti Chiron',
            "Price":'5.000.000 $'
        },
        {
            "img":"https://static0.carbuzzimages.com/wordpress/wp-content/uploads/2024/07/pagani-huayra-epitome_2-1-4_anteriore_portiera-guidatore-chiusa.jpg",
            "Name" : 'Pagani Model Huayra',
            "Price":'100.000.000 $'
        },
        {
            "img":"https://th.bing.com/th/id/OIP.l8jlHIFDSDEM44psOyS1FwHaE8?rs=1&pid=ImgDetMain",
            "Name" : "Mercedes AMG Clase G63",
            "Price":'12.000.000 $',
        },
        {
            "img": "https://th.bing.com/th/id/OIP.TbVf1ncnjcku2QYFyTZc6QHaEK?rs=1&pid=ImgDetMain",
            "Name": "Porhse Panamera",
            "Price": '12.000.000 $',
        },
        {
            "img": "https://th.bing.com/th/id/OIP.W8yCC3teVPrOuhJOJnRjdwHaEK?rs=1&pid=ImgDetMain",
            "Name": "Lamborghini Urus",
            "Price": '24.000.000 $',
        }, {
            "img":"https://th.bing.com/th/id/R.2c4041d9df9f17aaa0bec871c9f85108?rik=8umEt1Fu3PT%2bNQ&pid=ImgRaw&r=0",
            "Name" : 'Honda Civic',
            "Price":'1.000.000$'
        }
    ]
}

@app.route("/hola",methods=['GET'])
def mandar_mensaje():
    return "Hola "
@app.route("/data",methods=['GET'])
def send_data():
    return render_template("index.html",carros=data['cars'])

@app.route("/pedir",methods=['GET'])
def pedir():
    return  {
            "img":"https://static0.carbuzzimages.com/wordpress/wp-content/uploads/2024/07/pagani-huayra-epitome_2-1-4_anteriore_portiera-guidatore-chiusa.jpg",
            "Name" : 'Pagani model Huayra',
            "Price":'10000$'
        }


@app.route("/saludar/<nombre>",methods=['GET'])

def saludar(nombre):
    return f'Hola {nombre}'
@app.route('/confirmacion')
def confirmacion():
    return render_template('compras.html')


@app.route('/nombre/<nombre>') #CUANDO SE RECIBE ALGO
def json(nombre):
    return jsonify({'nombre':nombre.lower()})

@app.route('/int/<int:num>')
def mostrar_edad(num):
    return f'El numero es {num}'




