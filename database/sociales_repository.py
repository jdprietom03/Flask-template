from model.Social import Social
from database.Entity import RepositoryInitiator, Repository

@RepositoryInitiator(Type = Social, collection = "sociales")
class SocialRepository(Repository):
    pass 