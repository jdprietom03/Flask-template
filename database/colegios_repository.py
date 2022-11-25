from model.Colegio import Colegio
from database.Entity import RepositoryInitiator, Repository

@RepositoryInitiator(Type = Colegio, collection = "colegios")
class ColegioRepository(Repository):
    pass 