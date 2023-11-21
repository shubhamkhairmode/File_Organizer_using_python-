import os, sys
import shutil
from flask import Flask, request, render_template
from utils.common import get_file_extension, create_directory
app = Flask(__name__)


def organize_file(source_directory):
    
    if not os.path.exists(source_directory):
        
        print("Our Scource Directory is not exists")
        return
    
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)
        
        if os.path.isfile(file_path):
            extension = get_file_extension(filename)
            if extension:
                destenation_direcotry = os.path.join(source_directory, extension[1:])
                create_directory(destenation_direcotry)
                
                try:
                    shutil.move(file_path, os.path.join(destenation_direcotry, filename))
                    print(f"Moved succesfully '{filename}' to '{destenation_direcotry}'")
                except Exception as e:
                    
                    print(f"Moving Error '{filename}' to '{destenation_direcotry}': {e}")
                    
            else:
                print(f"skipped '{filename}' as its doesen't have any types of extention.")
                
        else:
            print(f"Skipped '{filename}' as is is not a file")
                  
    print("Our Complete File is Organized")

# localhost:5000
@app.route('/', methods = ['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        source_directory = request.form['source_directory']
        message = organize_file(source_directory)

    return render_template('index.html', message = message)

if __name__ == '__main__':
    app.run(debug=True)

