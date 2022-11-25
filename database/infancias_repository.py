from model.Infancia import Infancia
from database.Entity import RepositoryInitiator, Repository

@RepositoryInitiator(Type = Infancia, collection = "infancias")
class InfanciaRepository(Repository):
    pass 