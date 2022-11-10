class Carro: #Se crea una clase
    def __init__(self, request): #Constructor, recibimos el self y request (peticion)
        self.request = request #Almacenamos la petición actual para luego usarla
        self.session = request.session #Tenemos inicada la sesión
        carro = self.session.get("carro") #Construimos un carro de la compra para esta sesión
        #Cuando el usuario agrega un articulo, tenemos que igualar la sesión el usuario con ese carro
        
        #Si el usuario se va, tiene que verificar que tenga carro 
        if not carro: 
            carro = self.session["carro"]={} #Crea un diccionario.
        
        self.carro = carro #Usa la que ya estaba
    
    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={ #Lo agrega al diccionario
                "producto_id":producto.id,  #Clave y valor
                "nombre": producto.name,
                "precio": str(producto.pvp),
                "cantidad": 1, #Aqui se puede cambiar para obtener algún numero
                "imagen": producto.image.url,
                "subtotal": str(producto.pvp) #Se creo para mostrar el subtotal
            }
        else:
            for key, value in self.carro.items():
                if key ==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["subtotal"]= str(float(value["precio"])*int(value["cantidad"]))
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified = True
    
    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
        
    def restar_producto(self, producto):
        for key, value in self.carro.items():
                if key ==str(producto.id):
                    value["precio"]=str(producto.pvp)
                    value["cantidad"]=value["cantidad"]-1
                    value["subtotal"]= str(float(value["precio"])*int(value["cantidad"]))
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
