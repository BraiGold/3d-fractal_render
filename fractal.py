# cambiar este valor para cambiar la "definicion"
CANTIDAD_DE_PASOS_TOTALES = 5
COLOR = None

import bpy

def blender_borrar_pantalla(excepto=['Camera','Light']):
    for el in bpy.data.objects:
        if el.name not in excepto:
            bpy.data.objects.remove(el)

    
def suma(t1, t2):
    return tuple(p + q for p,q  in zip(t1,t2))
        
def mult(constante, tupla):
    return tuple(constante * t for t in tupla)


def avanzar_un_paso(inicial, anterior, paso):
    extendido = anterior * 4
    siguiente = []
    
    for i in range(len(extendido)):
        siguiente.append(suma( extendido[i], mult(2**paso, inicial[i // ( len(extendido) // 4) ]) ) )
    
    return siguiente


def generar_fractal(pasos_totales):

    inicial = [(1,1,-1),(-1,1,1),(-1,-1,-1),(1,-1,1)]

    siguiente = inicial
    for paso in range(1, pasos_totales):
        siguiente = avanzar_un_paso(inicial, siguiente, paso)
    
    return siguiente
            
def blender_dibujar_cubos(coords, color=(1,1,1,1)):
    for coord in coords:
        bpy.ops.mesh.primitive_cube_add(location=coord)
        if color is not None:
            cube = bpy.context.active_object
            material = bpy.data.materials.new('mat_' + cube.name)
            material.diffuse_color = color#(float(.5),0.0, 1, 1.0)
            cube.active_material = material
   

def dibujar_fractal(pasos_totales, color=(1,1,1,1) ):
    coords = generar_fractal(pasos_totales)
    blender_dibujar_cubos(coords, color)




blender_borrar_pantalla()
dibujar_fractal(CANTIDAD_DE_PASOS_TOTALES, color= COLOR)

# OTRA COSA QUE SE PUEDE HACER:
#colores = [(0.5,0,1,1), (1,0.5,1,1), (1,1,0.5,1), (1,1,1,1)]
#for pasos_totales in range(1,CANTIDAD_DE_PASOS_TOTALES + 1):
#    dibujar_fractal(pasos_totales, colores[pasos_totales % len(colores)])
