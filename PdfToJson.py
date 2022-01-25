import PyPDF2
import json

# main function
def main():
    path = ""
    #get the name of pdf file and creat json file
    while(True):
        path = input("Enter Name of Article:")
        path += ".pdf"
        get_info(path)

def get_info(path):
    # get json sample format
    json_file = {}
    with open('output.json', 'r') as f:
        json_file = json.load(f)
    # read file from input path
    try:
        with open(path,'rb') as p:
            pdf_file = PyPDF2.PdfFileReader(p, strict= False)
            # get Document Info fram PdfFileReader
            doc_info = pdf_file.getDocumentInfo()
        # get info fram getDocumentInfo and put in json sample format
        for info in doc_info:
            json_file = add_info_json(json_file, info.replace('/','').lower(), doc_info[info])
        #creat json file as a name of pdf
        create_json(json_file, path)
    except IOError:
        print("Could not find the file name is {}".format(path))

# function that get json object, key and value add to json object and return
def add_info_json(json_file,key,value) -> dict:
    if( key in json_file):
        json_file[key] = value
    return json_file

#creat json file by input dict and file name
def create_json(json_file, filename):
    with open(filename.replace(".pdf", ".json"), 'w') as f:
        json.dump(json_file, f, indent= 4)
    print("Creat a new {} file\n".format(filename.replace(".pdf", ".json")))
   

if __name__ == '__main__':
    main()