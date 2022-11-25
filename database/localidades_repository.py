from model.Localidad import Localidad
from database.Entity import RepositoryInitiator, Repository

@RepositoryInitiator(Type = Localidad, collection = "localidades")
class LocalidadRepository(Repository):
    pass 