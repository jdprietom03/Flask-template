from database.firebase import db

def RepositoryInitiator(Type = None, collection = ""):
    def wrapper(repository_class):
        class_init = repository_class.__init__
        def __init__(self, *args, **kws):
            class_init(self, Type, collection = collection, *args, **kws)

        repository_class.__init__ = __init__

        return repository_class
    
    return wrapper

class Repository:

    def __init__(self):
        self.__collection = ""

    def __init__(self, Type, collection = ""):
        self.__collection = collection
        self.Type = Type

    def get_all(self):
        collection_ref = db.collection(self.__collection)
        docs = collection_ref.stream()
        elements = []

        for doc in docs:
            elements.append(self.Type(doc.to_dict(), id=doc.id))
        
        return elements

    def get(self, id):
        doc_ref = db.collection(self.__collection).document(id)
        doc = doc_ref.get()
        if doc.exists:
            return self.Type(doc.to_dict(), id=doc.id)
        else:
            return None

    def create(self, object):
        doc_ref = db.collection(self.__collection).document()
        doc_ref.set(object.__dict__)
        return self.Type(object.__dict__, id=doc_ref.id)

    def update(self, object, id):
        doc_ref = db.collection(self.__collection).document(id)
        doc_ref.update(object.__dict__)
        return self.Type(object.__dict__, id=id)

    def delete(self, id):
        doc_ref = db.collection(self.__collection).document(id)
        doc_ref.delete()
