from sqlalchemy import Column,ForeignKey, BigInteger,Integer, String, TIMESTAMP, text
# Importaciones
from Api.Data.conection import ConexionBD


class BinnacleData(ConexionBD.Base): 
    __tablename__ = "binnacles"
    
    id = Column(BigInteger, primary_key=True, index=True)
    action = Column(String(100))
    error = Column(String(300))
    status_code = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    
    def __str__(self):
        return f"Binnacle(id={self.id}, action={self.action}, error={self.error}, status_code={self.status_code}, created_at={self.created_at})"
    
    