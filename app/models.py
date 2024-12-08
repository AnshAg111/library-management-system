from bson import ObjectId

def format_id(document):
    """Convert MongoDB ObjectId to string for JSON serialization."""
    document["_id"] = str(document["_id"])
    return document

class BookModel:
    def __init__(self, db):
        self.collection = db.books

    def get_all(self):
        return [format_id(book) for book in self.collection.find()]

    def get_by_id(self, id):
        return format_id(self.collection.find_one({"_id": ObjectId(id)}))

    def create(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def update(self, id, data):
        self.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True

    def delete(self, id):
        self.collection.delete_one({"_id": ObjectId(id)})
        return True
    
    def search(self, title='', author='', page=1, per_page=10):
        """Search for books by title or author with pagination."""
        query = {}
        if title:
            query['title'] = {'$regex': title, '$options': 'i'}  
        if author:
            query['author'] = {'$regex': author, '$options': 'i'} 

        cursor = self.collection.find(query).skip((page - 1) * per_page).limit(per_page)
        return [format_id(book) for book in cursor]

class MemberModel:
    def __init__(self, db):
        self.collection = db.members

    def get_all(self):
        return [format_id(member) for member in self.collection.find()]

    def get_by_id(self, id):
        return format_id(self.collection.find_one({"_id": ObjectId(id)}))

    def create(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def update(self, id, data):
        self.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True

    def delete(self, id):
        self.collection.delete_one({"_id": ObjectId(id)})
        return True
