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
        return node.childNodes[0].data.encode('utf-8')
    def parse(self):
        node_root = self.xml_file.documentElement
        node_book_list = self.getNodeName(node_root,"book")
        for node_book in node_book_list:
            book_info = dict()
            node_book_title = self.getNodeName(node_book,"title")[0]
            book_title_value = self.getNodeValue(node_book_title)
            book_info["title"] = book_title_value

            node_book_author = self.getNodeName(node_book,"author")[0]
            book_author_value = self.getNodeValue(node_book_author)
            book_info['author'] = book_author_value

            node_book_year = self.getNodeName(node_book,'year')[0]
            book_year_value = self.getNodeValue(node_book_year)
            book_info['year'] = book_year_value

            node_book_price = self.getNodeName(node_book,'price')[0]
            book_price_value = self.getNodeValue(node_book_price)
            book_info['price'] = book_price_value

            self.book_list.append(book_info)
            
    def getList(self):
        return self.book_list

if __name__ == "__main__":
    myXmlPaser = xmlParser("test.xml")
    myXmlPaser.parse()
    book = myXmlPaser.getList()
    for node in book:
        print node['author']
    
            

