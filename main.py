from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from core import Core
from model.users import Users
import re

dbconfig = Core.config.database
engine = create_engine(f"mysql+mysqlconnector://{dbconfig.login.user}:{dbconfig.login.password}@{dbconfig.host}:{dbconfig.port}/{dbconfig.name}")

Session = sessionmaker(bind=engine)
session = Session()

idregex = r'[a-zA-Z0-9_.]{1,30}'
regex = r'@('+idregex+')|([^a-z]ig|[^a-z]ins[a-z]{0,6}|[^a-z]inst[a-z]{0,6}|[^a-z]insta[a-z]{0,6}|instagram)( : |: |:| )('+idregex+')( |)'

# Exécution de la requête SQL avec expression régulière
query = session.query(Users).filter(Users.bio.op('regexp')(regex))
results = query.all()

# Récupération des données en tant qu'objets Python
for user in results:
    resultat = re.search(regex, str(user.bio).lower())
    if resultat:
        ig = resultat.group(4) if resultat.group(1) is None else resultat.group(1)
        print(f"[{user.id}] ({user.name}) {ig}")
    else:
        print(f"id:{user.id}\nbio:{user.bio}")
        raise "La REGEX de la requête SQL à trouvé un profil, mais Python ne trouve pas le ocmpte Instagram"

# Fermeture de la session
session.close()
