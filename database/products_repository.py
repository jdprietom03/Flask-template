from model.Product import Product
from database.Entity import RepositoryInitiator, Repository



@RepositoryInitiator(Type = Product, collection = "products")
class ProductRepository(Repository):
    pass 