from model.Ciudadano import Ciudadano
from database.Entity import RepositoryInitiator, Repository



@RepositoryInitiator(Type = Ciudadano, collection = "ciudadanos")
class CiudadanoRepository(Repository):
    def set_beneficios_sociales(self, total):
        ciudadanos = self.get_all()
        for ciudadano in ciudadanos:
            ciudadano.BPPS = "F"
            self.update(ciudadano, ciudadano.document_id)
            
        # Select total random ciudadanos
        import random
        random.shuffle(ciudadanos)
        ciudadanos = ciudadanos[:min(len(ciudadanos), total)]

        for ciudadano in ciudadanos:
            ciudadano.BPPS = "T"
            self.update(ciudadano, ciudadano.document_id)

        return [ total - len(ciudadanos), len(ciudadanos) ]

    def filter_by_BPPS(self, value):
        ciudadanos = self.get_all()
        return [ ciudadano for ciudadano in ciudadanos if ciudadano.BPPS == value ]

    def filter_by_BPPI(self, value):
        ciudadanos = self.get_all()
        return [ ciudadano for ciudadano in ciudadanos if ciudadano.BPPI == value ]

    def set_beneficios_infancia(self, total):
        ciudadanos = self.get_all()
        for ciudadano in ciudadanos:
            ciudadano.BPPI = "F"
            self.update(ciudadano, ciudadano.document_id)
            
        # Select total random ciudadanos
        import random
        random.shuffle(ciudadanos)
        ciudadanos = ciudadanos[:min(len(ciudadanos), total)]

        for ciudadano in ciudadanos:
            ciudadano.BPPI = "T"
            self.update(ciudadano, ciudadano.document_id)

        return [ total - len(ciudadanos), len(ciudadanos) ]
