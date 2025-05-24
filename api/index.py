
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Your original list of students
students_list = [{"name":"Jo4t7r","marks":74},{"name":"FBuF2rvb","marks":91},{"name":"SLgg","marks":66},{"name":"cMsxZhZCCj","marks":40},{"name":"ZfG","marks":99},{"name":"kutpjL9","marks":11},{"name":"AV","marks":70},{"name":"ZEjZer","marks":99},{"name":"ZCzV1e8Bfh","marks":81},{"name":"YL9rt9","marks":29},{"name":"prts2i7fI","marks":7},{"name":"8v","marks":2},{"name":"vS","marks":82},{"name":"Lre","marks":40},{"name":"xpi","marks":55},{"name":"IyX","marks":83},{"name":"5LariF","marks":22},{"name":"S9zHDGbU4D","marks":9},{"name":"HsQyh8iukM","marks":44},{"name":"fEIT4994p","marks":66},{"name":"9I5X","marks":3},{"name":"Q","marks":56},{"name":"g","marks":8},{"name":"mG","marks":89},{"name":"h","marks":12},{"name":"EQ54WmKjM","marks":36},{"name":"3on2kz6t","marks":97},{"name":"g9G2I","marks":27},{"name":"VbVX","marks":7},{"name":"DEDIbcsycl","marks":33},{"name":"0dN","marks":3},{"name":"4Ym","marks":12},{"name":"l8WwZ2o","marks":93},{"name":"SPqDv5fbaX","marks":3},{"name":"MG","marks":81},{"name":"RJ","marks":84},{"name":"nGF","marks":92},{"name":"DRWwXh","marks":87},{"name":"4NXs6gi","marks":99},{"name":"Pe","marks":98},{"name":"7prRW","marks":17},{"name":"yuxo","marks":13},{"name":"1","marks":96},{"name":"VweKEA1","marks":29},{"name":"gzpascHZeH","marks":36},{"name":"rfLT","marks":68},{"name":"es8H9eqcoN","marks":82},{"name":"Eyt","marks":24},{"name":"9VfDJ791","marks":44},{"name":"OoKP","marks":56},{"name":"caLP","marks":72},{"name":"z3","marks":41},{"name":"NkuE0","marks":48},{"name":"gOpM4Kv","marks":40},{"name":"jOBY","marks":32},{"name":"SmZoKW","marks":41},{"name":"vPbrgcJ","marks":56},{"name":"aFM3dChx4","marks":53},{"name":"KXDH","marks":41},{"name":"a06","marks":76},{"name":"tvu9L","marks":56},{"name":"q","marks":56},{"name":"pnR2Xya","marks":7},{"name":"PhRwnE","marks":69},{"name":"6JqzQm0W","marks":55},{"name":"nlrxh","marks":92},{"name":"Bc","marks":72},{"name":"b0e1wg","marks":77},{"name":"E","marks":26},{"name":"7qkR","marks":22},{"name":"2CH","marks":44},{"name":"9A5adNPHbd","marks":20},{"name":"KrNmQfNUYm","marks":10},{"name":"kstDKD5j","marks":89},{"name":"p4Eg","marks":62},{"name":"Hl","marks":35},{"name":"TkdupSXZ","marks":18},{"name":"Tz","marks":6},{"name":"Wz0g1qOw","marks":22},{"name":"0i","marks":56},{"name":"QZ","marks":97},{"name":"US","marks":52},{"name":"LG","marks":40},{"name":"bC","marks":58},{"name":"Z","marks":29},{"name":"RelDw2D6","marks":41},{"name":"W06Ud3K","marks":67},{"name":"PiuqtaJ","marks":69},{"name":"3grQmZI","marks":6},{"name":"Fk7P","marks":6},{"name":"tsM9z3","marks":49},{"name":"gmr47E","marks":85},{"name":"RTH9Nrzyxq","marks":29},{"name":"7","marks":77},{"name":"L","marks":64},{"name":"uKREpyio","marks":4},{"name":"fnz1","marks":28},{"name":"vQ8q","marks":80},{"name":"GxOb","marks":2},{"name":"cL3vaTEA","marks":69}]

# Convert list to dictionary for fast lookup
students = {student["name"]: student["marks"] for student in students_list}

@app.route('/', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [students.get(name, 0) for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run()
