import xml.dom.minidom as Dom
import sys
class xmlParser():
    def __init__(self, xml_file_path):
        try:
            self.xml_file = Dom.parse(xml_file_path)
        except:
            sys.exit()
        self.book_list = list()

    def getNodeName(self,prev_node,node_name):
        return prev_node.getElementsByTagName(node_name)
    def getNodeAttr(self,node,att_name):
        return node.getAttribute(att_name)
    def getNodeValue(self,node):
        return node.childNodes[0]
    def parse(self):
        self.node_root = self.xml_file.documentElement
        node_book_list = self.getNodeName(self.node_root,"book")
        for node_book in node_book_list:
            book_info = dict()
            book_category = self.getNodeAttr(node_book,'category')
            book_info['category'] = book_category
            node_book_title = self.getNodeName(node_book,"title")[0]
            book_title_value = self.getNodeValue(node_book_title)
           # book_title_value.nodeValue = 'learn xml'
            book_info["title"] = book_title_value.nodeValue

            node_book_author = self.getNodeName(node_book,"author")[0]
            book_author_value = self.getNodeValue(node_book_author)
          #  book_author_value.nodeValue= 'chenjia'
            book_info['author'] = book_author_value.nodeValue

            node_book_year = self.getNodeName(node_book,'year')[0]
            book_year_value = self.getNodeValue(node_book_year)
          #  book_year_value.nodeValue = '2013'
            book_info['year'] = book_year_value.nodeValue

            node_book_price = self.getNodeName(node_book,'price')[0]
            book_price_value = self.getNodeValue(node_book_price)
           # book_price_value.nodeValue =raw_input(book_price_value.nodeValue+'\n')
            book_info['price'] = book_price_value.nodeValue

            self.book_list.append(book_info)
            
    def getList(self):
        return self.book_list
    def xmlWrite(self):
        f = open('test.xml','w')
#        f.write(self.node_root.toxml())
        self.node_root.writexml(f)
        f.close()


class constructXml():
    def __init__(self):
        self.doc = Dom.Document()#create Dom object
        self.bookstore = self.doc.createElement('bookstore') #create root element
        self.bookstore.setAttribute('address','xinghuaRoad') #set attribute
        self.doc.appendChild(self.bookstore)  #add root node
        
    def addBook(self,bookData):
        book = self.doc.createElement('book')
        book.setAttribute('category',bookData['category'])
        self.bookstore.appendChild(book)
        
        title = self.doc.createElement('title')
        title_text = self.doc.createTextNode(bookData['title'])
        title.appendChild(title_text)
        book.appendChild(title)
        
        author = self.doc.createElement('author')
        author_text = self.doc.createTextNode(bookData['author'])
        author.appendChild(author_text)
        book.appendChild(author)
        
        year = self.doc.createElement('year')
        year_text = self.doc.createTextNode(bookData['year'])
        year.appendChild(year_text)
        book.appendChild(year)
        
        price = self.doc.createElement('price')
        price_text = self.doc.createTextNode(bookData['price'])
        price.appendChild(price_text)
        book.appendChild(price)
        
        print self.doc.toprettyxml()
        
        def xmlWrite(self):
            f = open('test.xml','w')
#            f.write(self.node_root.toxml())
            self.doc.writexml(f)
            f.close()

if __name__ == "__main__":
    myXmlPaser = xmlParser("test.xml")
    myXmlPaser.parse()
    test = constructXml()
    book = myXmlPaser.getList()

    for node in book:
        print '_____________________'
        for key in node:
            print node[key]
        print '_____________________'

    for node in book:
        print "====================="
        test.addBook(node)
        print "====================="
        
    myXmlPaser.xmlWrite()

