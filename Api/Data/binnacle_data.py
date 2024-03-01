from sqlalchemy import Column,ForeignKey, BigInteger,Integer, String, TIMESTAMP, text
# Importaciones
from Api.Data.conection import ConexionBD


class BinnacleData(ConexionBD.Base): 
    __tablename__ = "binnacles"
    
    id = Column(BigInteger, primary_key=True, index=True)
    endpoint = Column(String(100))
    method = Column(String(100))
    detail = Column(String(300))
    status_code = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    ip_client = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=text("now()"))
    
    def __str__(self):
        return f"BinnacleData(id={self.id}, endpoint={self.endpoint}, method={self.method}, detail={self.detail}, status_code={self.status_code}, user_id={self.user_id}, ip_client={self.ip_client}, created_at={self.created_at})"
    