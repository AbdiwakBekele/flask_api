from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"







# from flask import Flask, request, jsonify
# # import werkzeug

# app = Flask(__name__)

# # @app.route('/upload', methods=["POST"])
# # def upload():
# #     if(request.method == "POST"):
# #         # imagefile = request.files['image']
# #         # filename = werkzeug.utils.secure_filename(imagefile.filename)
# #         # imagefile.save("./uploadedimages/" + filename)
# #         return jsonify({
# #             "message": "Image Uploaded Successfully"
# #         })
        
# # @app.route('/', methods=["POST"])
# @app.route('/')
# def hello_world():
#     return "Hello World"
#     # return jsonify({
#     #         "message": "Image Uploaded Successfullyyyyyyyyy"
#     #     })
        

# if __name__ == "__main__":
#     app.run()
    
    
    
    
# # For Flutter App
# # final request = http.MultipartRequest(
# #               "POST", Uri.parse("http://melkamtechnology.com/flask_api/"));

# #           final headers = {"Content-type": "multipart/form-data"};

# #           request.headers.addAll(headers);
# #           final response = await request.send();
# #           http.Response res = await http.Response.fromStream(response);
# #           final resJson = jsonDecode(res.body);
# #           message = resJson['message'];
# #           setState(() {});



