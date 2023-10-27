from domain.solicitudmarca import solicitud
from domain.createauto import createauto
from view.modoview import modo

if modo == "comprar":
        def main():

                marca = solicitud.main()
                print(marca)
elif modo == "agregar":   
        def main():
            
                auto = createauto.main()
                print(auto)
                
