from domain.solicitudmarca import solicitud
from domain.createauto import createauto
from controller.modocontroller import mododeuso

if mododeuso == "comprar":
        def main():

                marca = solicitud.main()
                print(marca)
elif mododeuso == "agregar":   
        def main():
            
                auto = createauto.main()
                print(auto)
                
