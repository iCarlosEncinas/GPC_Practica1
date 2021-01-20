from OpenGL.GL import *
from glew_wish import *
import glfw
import random

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana
    #independientemente del SO que usemos
    window = glfw.create_window(800,600,'Mi ventana', None, None)

    #configuracimos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)


    #Activamos la validación funciones modernas de OpenGL
    glewExperimental = True

    #inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return
    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece región de dibujo
        glViewport(0,0,800,600)
        #Establece color de borrado

        r = random.random()
        g = random.random()
        b = random.random()
        a = random.random()

        glClearColor(r,g,b,a)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar

        #PReguntar si ubo entradas de perifericos
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #termina los procesos que inició
    glfw.terminate()

if __name__ == "__main__":
    main()
