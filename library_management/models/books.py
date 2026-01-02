class book():

    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.isAvailable = True
    
    def issue(self):
        self.isAvailable = False
    
    def return_book(self):
        self.isAvailable = True