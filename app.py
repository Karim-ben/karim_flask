from flask import Flask, jsonify,request

import pandas as pd
import json





app = Flask(__name__)



@app.route('/upload', methods=['POST'])
def upload():
    try:
        uploaded_file = request.files['excelFile']
        uploaded_file.save('uploaded_file.xlsx')
        # read excel file

        df=pd.read_excel('./uploaded_file.xlsx',usecols="D",skiprows=range(1,15))
        df1=pd.read_excel('./uploaded_file.xlsx',usecols="D")
        df2=pd.read_excel('./uploaded_file.xlsx',usecols="O")
        df3=pd.read_excel('./uploaded_file.xlsx',usecols="O")
        df4=pd.read_excel('./uploaded_file.xlsx',usecols="I")
      

        df=df.dropna()
        df1=df1.dropna()
        df2=df2.dropna()
        df3=df3.dropna()
        df4=df4.dropna()
        
        df1=df1.iloc[[2]]
        df2=df2.iloc[[3]]
        df3=df3.iloc[[4]]
        df4=df4.iloc[[3]]
        
        length_of_df = df.shape[0]

        # print(f"Length of DataFrame: {length_of_df} rows")
        df.insert(1,"N0",[i for i in range(length_of_df)])
         # Convert DataFrame to JSON
        df_json = df.to_json(orient='records')
        df1_json = df1.to_json(orient='records')
        df2_json = df2.to_json(orient='records')
        df3_json = df3.to_json(orient='records')
        df4_json = df4.to_json(orient='records')
       
        # Parse JSON string to Python dictionary
        data = json.loads(df_json)
        name_classe=json.loads(df1_json)
        prof_name=json.loads(df2_json)
        matier_name=json.loads(df3_json)
        type_classe=json.loads(df4_json)
        

        return jsonify({"data": data,"classe":name_classe,"prof":prof_name,"matiere":matier_name,"type":type_classe}), 200, {'Access-Control-Allow-Origin': '*'}
        # # Perform any processing with the uploaded file (e.g., save it, parse it, etc.)
        # # For demonstration purposes, let's save it to the server's filesystem
        # uploaded_file.save('uploaded_file.xlsx')

        # return jsonify({'data': 'success', 'message': 'File uploaded successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/')
def hello_world():
    return 'hello world'

