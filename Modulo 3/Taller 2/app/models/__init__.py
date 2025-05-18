from app.models.gato import Gato
from app.models.perro import Perro
from app.models.huron import Huron
from app.models.boa import Boa_Constrictor as Boa

Cat = Gato("Gato", "", 0, 0)
Dog = Perro("Perro", "", 0, 0)
Ferret = Huron("Hurón", 0, 0, "", 0)
Snake = Boa("Boa Constrictor", 0, 0, "", 0)