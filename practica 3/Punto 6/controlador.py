from manejadorprovincias import ManejadorProvincias
from vista import ProvinciaView
from form import NewProvincia
from repositorio import RespositorioProvincias

class ControladorProvincias():
    
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.provincias = list(repo.obtenerListaProvincias())
    
    def crearProvincia(self):
        nuevoProvincia = NewProvincia(self.vista).show()
        if nuevoProvincia:
            provincia = self.repo.agregarProvincia(nuevoProvincia)
            self.provincias.append(provincia)
            self.vista.agregarProvincia(provincia)

    def seleccionarProvincia(self, index):
        self.seleccion = index
        provincia = self.provincias[index]
        self.vista.verProvinciaEnForm(provincia)

    def start(self):
        for p in self.provincias:
            self.vista.agregarProvincia(p)
        self.vista.mainloop()

    def salirGrabarDatos(self):
        self.repo.grabarDatos()