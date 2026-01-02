class library_services():
    def get_all_books(self):
        return books
    def issue_book(self, title):
        for book in books:
            if book.title == title:
                if book.isAvailable:
                    book.issue()
                    return f"{title} has be assigned successfully"
                else:
                    return f"{title} is assigned to someone else"
        return f"sorry {title} is not available"
    
    def student_return_book(self , title):
        for book in books:
            if book.title == title:
                book.return_book()
                return f"{title} has been returned successfully"
        return f"{title} is not the property of library"
