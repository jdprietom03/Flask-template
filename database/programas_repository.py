from model.Programa import Programa
from database.Entity import RepositoryInitiator, Repository

@RepositoryInitiator(Type = Programa, collection = "programas")
class ProgramaRepository(Repository):
    pass 