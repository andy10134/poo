from repositorio import RespositorioPacientes
from vista import PacienteView
from objectEncoder import ObjectEncoder
# from claseControladorContactos import ControladorContactos

def main():
    pac = ObjectEncoder('pacientes.json')
    repo = RespositorioPacientes(pac)
    vista = PacienteView()
    ctrl = ControladorContactos(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()
