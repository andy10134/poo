from repositorio import RespositorioPacientes
from vista import ContactsView
from objectEncoder import ObjectEncoder
# from claseControladorContactos import ControladorContactos

def main():
    pac = ObjectEncoder('pacientes.json')
    repo = RespositorioPacientes(pac)
    vista = ContactsView()
    # ctrl = ControladorContactos(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()
