from repositorio import RespositorioPacientes
from vista import PacienteView
from objectEncoder import ObjectEncoder
from controlador import ControladorPacientes

def main():
    pac = ObjectEncoder('pacientes.json')
    repo = RespositorioPacientes(pac)
    vista = PacienteView()
    ctrl = ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()
