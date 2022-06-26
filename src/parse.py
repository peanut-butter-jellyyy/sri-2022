
from http.client import LineTooLong
from cv2 import line
from pyrsistent import field
from structs import Document
from structs import Query







def parse_relevancies(path):
    file = open(path,"r+")
    relevancies = {}
    
    while True:
        line = file.readline()
        if not line:
            return relevancies
        
        line_splited = line.split(' ')
        try:
            relevancies[int(line_splited[0])].add(int(line_splited[1]))
        except KeyError:
            relevancies[int(line_splited[0])] = set()
            relevancies[int(line_splited[0])].add(int(line_splited[1]))


def parse_queries(path):
    file = open(path,"r+")
    query_list = []
    query = None
    sections = {".I":1,".W":2}
    
    
    while True:
        line = file.readline()
        if not line:
            if query:
                query_list.append(query)
                query = None
            return query_list
        else:
            line_split = line.split(' ',1)
            line0 = line_split[0].split("\n")[0]
            if line0 in sections:
                section = sections[line0]
                if section == 1:
                    if query:
                        query_list.append(query)
                        query = Query()
                        id = line_split[1].split('\n')[0]
                        query.id = int(id)
                    else:
                        query = Query()
                        id = line_split[1].split('\n')[0]
                        query.id = int(id)
            else:
                if section == 2:
                    line1 = line.split('\n')[0]
                    query.body += " " 
                    query.body += line1



def parse_documents(path):
    file = open(path,"r+")
    document_list = []
    document = None
    sections = {".I":1,".T":2,".A":3,".B":4,".W":5}
    
    while True:
        line = file.readline()
        if not line:
            if document:
                document_list.append(document)
                document = None
            return document_list
        else:
            line_split = line.split(' ',1)
            line0 = line_split[0].split("\n")[0]
            if line0 in sections:
                section = sections[line0]
                if section == 1:
                    if document:
                        document_list.append(document)
                        document = Document()
                        id = line_split[1].split('\n')[0]
                        document.id = int(id)
                    else:
                        document = Document()
                        id = line_split[1].split('\n')[0]
                        document.id = int(id)
                
            else:
                if section == 2:
                    line1 = line.split('\n')[0]
                    document.body += " " 
                    document.body += line1
                elif section == 3:
                    line1 = line.split('\n')[0]
                    document.body += " " 
                    document.body += line1
                elif section == 4:
                    line1 = line.split('\n')[0]
                    document.body += " " 
                    document.body += line1                
                elif section == 5:
                    line1 = line.split('\n')[0]
                    document.body += " " 
                    document.body += line1 
            
                
                
        