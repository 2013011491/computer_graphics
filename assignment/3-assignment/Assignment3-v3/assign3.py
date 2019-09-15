import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from OpenGL.arrays import vbo
import ctypes

gCamAng = 0.
gCamHeight = 1.
gZoom = 1.
normal=[]
zmode=GL_FILL


def render(ang):
        global gCamAng, gCamHeight, gZoom,normal,zmode
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glEnable(GL_DEPTH_TEST)
        glPolygonMode( GL_FRONT_AND_BACK, zmode)
        glMatrixMode(GL_PROJECTION) # use projection matrix stack for projectiontransformation for correct lighting
        glLoadIdentity()
        gluPerspective(45, 1, 1,10)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        gluLookAt((5*np.sin(gCamAng))*gZoom,gCamHeight*gZoom,(5*np.cos(gCamAng))*gZoom, 0,0,0, 0,1,0)

        drawFrame()

        glEnable(GL_LIGHTING)   # try to uncomment: no lighting
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)

        # light position
        glPushMatrix()

        # glRotatef(ang,0,1,0) # try to uncomment: rotate light
        lightPos = (3.,3.,3.,1.)
        lightPos1 = (-3.,3.,-3.,1.)

        # try to change 4th element to 0. or 1.
        glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
        glLightfv(GL_LIGHT1, GL_POSITION, lightPos1)
        glPopMatrix()

        # light intensity for each color channel
        ambientLightColor = (.1,.1,.1,1.)
        diffuseLightColor = (1.,1.,1.,1.)
        specularLightColor = (1.,1.,1.,1.)
        glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLightColor)
        glLightfv(GL_LIGHT0, GL_DIFFUSE,diffuseLightColor)
        glLightfv(GL_LIGHT0, GL_SPECULAR,specularLightColor)

        glLightfv(GL_LIGHT1, GL_AMBIENT, ambientLightColor)
        glLightfv(GL_LIGHT1, GL_DIFFUSE,diffuseLightColor)
        glLightfv(GL_LIGHT1, GL_SPECULAR,specularLightColor)

        # material reflectance for each color channel
        diffuseObjectColor = (1.0,1.0,1.0,1.)
        specularObjectColor = (1.,0.,0.,1.)
        glMaterialfv(GL_FRONT,GL_AMBIENT_AND_DIFFUSE, diffuseObjectColor)

        # glMaterialfv(GL_FRONT, GL_SPECULAR, specularObjectColor)
        glPushMatrix()
        # glRotatef(ang,0,1,0) 
        # try to uncomment: rotate object
        
        glColor3ub(0, 0, 255) # glColor*() is ignored if lighting is enabled
        
        drawUnitCube_glDrawElements()
        glPopMatrix()
        glDisable(GL_LIGHTING)

def drawFrame():
        glBegin(GL_LINES)
        glColor3ub(255, 0, 0)
        glVertex3fv(np.array([0.,0.,0.]))
        glVertex3fv(np.array([1.,0.,0.]))
        glColor3ub(0, 255, 0)
        glVertex3fv(np.array([0.,0.,0.]))
        glVertex3fv(np.array([0.,1.,0.]))
        glColor3ub(0, 0, 255)
        glVertex3fv(np.array([0.,0.,0]))
        glVertex3fv(np.array([0.,0.,1.]))
        glEnd()

def drop_callback(window,paths):
        global gVertexArrayIndexed, gIndexArray,normal
        f=open(paths[0],'r')
        print("1.File name : "+paths[0])
        content=f.read()
        eaLines=content.splitlines()
        varr=[]
        normal=[]
        iarr=[]
        inorm=[]
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_NORMAL_ARRAY)
        face3=0
        face4=0
        facei=0
        face=0
        
        for eaLine in eaLines :
                element = eaLine.split()
                if element==[]:
                        pass
                elif element[0] == 'v' :
                        v = np.array([float(element[1]), float(element[2]), float(element[3])])
                        varr.append(v)
                elif element[0] == 'vn' :
                        vn = np.array([float(element[1]), float(element[2]), float(element[3])])
                        normal.append(vn)
                elif element[0] == 'f' :
                        vf=np.array([0,0,0])
                        vs=np.array([0,0,0])
                        if len(element)==4:
                                face3 +=1
                                for i in range(1, len(element)):
                                              vf[i-1]=int(element[i].split('/')[0])-1
                                              vs[i-1]=int(element[i].split('/')[2])-1
                                inorm.append(vs)
                                iarr.append(vf)
                        #polygon more triangle
                        elif len(element) ==5 :
                                face4 +=1
                                for i in range(1, 4):
                                              vf[i-1]=int(element[i].split('/')[0])-1
                                              vs[i-1]=int(element[i].split('/')[2])-1
                                for i in range(4,len(element)):
                                        vf=np.append(vf,[int(element[i].split('/')[0])-1])
                                        vs=np.append(vs,[int(element[i].split('/')[2])-1])
                                vf.ravel()
                                vs.ravel()
                                iarr.append([vf[0],vf[1],vf[2]])
                                inorm.append([vs[0],vs[1],vs[2]])
                                for i in range(2, len(element)-2):
                                      iarr.append([vf[i],vf[i+1],vf[0]])
                                      inorm.append([vs[i],vs[i+1],vs[0]])
                        elif len(element) >5 :
                                facei +=1
                                for i in range(1, 4):
                                              vf[i-1]=int(element[i].split('/')[0])-1
                                              vs[i-1]=int(element[i].split('/')[2])-1
                                for i in range(4,len(element)):
                                        vf=np.append(vf,[int(element[i].split('/')[0])-1])
                                        vs=np.append(vs,[int(element[i].split('/')[2])-1])
                                vf.ravel()
                                vs.ravel()
                                iarr.append([vf[0],vf[1],vf[2]])
                                inorm.append([vs[0],vs[1],vs[2]])
                                for i in range(2, len(element)-2):
                                      iarr.append([vf[i],vf[i+1],vf[0]])
                                      inorm.append([vs[i],vs[i+1],vs[0]])
        
                else :
                        pass
                
        gVertexArrayIndexed=np.array(varr,'float32')
        gIndexArray=np.array(iarr)
        inorm=np.array(inorm)
        normal=np.array(normal)
        new=np.zeros((len(gVertexArrayIndexed),3))
        for i in range(0,len(gIndexArray)):
                for j in range(0,len(gIndexArray[i])):
                        new[gIndexArray[i][j],:]+=normal[inorm[i][j]]
        for i in range(0,len(new)):
                new[i]=normalized(new[i])
        normal=new
        f.close()
        print("2.Total number of faces : "+str(face3+face4+facei))
        print("3.Number of faces with 3 vertices : "+str(face3))
        print("4.Number of faces with 4 vertices : "+str(face4))
        print("5.Number of faces with more than 4 vertices : "+str(facei))
 
def key_callback(window, key, scancode, action, mods):
        global gCamAng, gCamHeight, gZoom,zbit,zmode
        if action==glfw.PRESS or action==glfw.REPEAT:
                if key==glfw.KEY_1:
                        gCamAng += np.radians(-10)
                elif key==glfw.KEY_3:
                        gCamAng += np.radians(10)
                elif key==glfw.KEY_2:
                        gCamHeight += .1
                elif key==glfw.KEY_W:
                        gCamHeight += -.1
                elif key==glfw.KEY_A:
                        gZoom *= 0.9
                elif key==glfw.KEY_S:
                        gZoom *= 1.1
                elif key==glfw.KEY_Z:
                        if zmode==GL_FILL:
                                zmode=GL_LINE
                        elif zmode==GL_LINE:
                                zmode=GL_FILL
def createVertexAndIndexArrayIndexed():
        global normal
        normal=np.array([normalized([1,1,-1]),
                         normalized([-1,1,-1]),
                         normalized([-1,1,1]),
                         normalized([1,1,1]),
                         normalized([1,-1,1]),
                         normalized([-1,-1,1]),
                         normalized([-1,-1,-1]),
                         normalized([1,-1,-1]),
                         ])
        varr = np.array([
                [ 0.5, 0.5,-0.5],
                [-0.5, 0.5,-0.5],
                [-0.5, 0.5, 0.5],
                [ 0.5, 0.5, 0.5],
                [ 0.5,-0.5, 0.5],
                [-0.5,-0.5, 0.5],
                [-0.5,-0.5,-0.5],
                [ 0.5,-0.5,-0.5],
                ], 'float32')
        iarr = np.array([
                [0,1,2],
                [0,2,3],
                [4,5,6],
                [4,6,7],
                [3,2,5],
                [3,5,4],
                [7,6,1],
                [7,1,0],
                [2,1,6],
                [2,6,5],
                [0,3,4],
                [0,4,7],
                ])
        return varr, iarr
def l2norm(v):
        return np.sqrt(np.dot(v, v))
def normalized(v):
        l = l2norm(v)
        return 1/l * np.array(v)
def drawUnitCube_glDrawElements():
        global gVertexArrayIndexed, gIndexArray,normal
        varr = gVertexArrayIndexed
        iarr = gIndexArray
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_NORMAL_ARRAY)
        glNormalPointer(GL_FLOAT, 0,normal)
        glVertexPointer(3,GL_FLOAT,3*varr.itemsize,varr)
        glDrawElements(GL_TRIANGLES, iarr.size,GL_UNSIGNED_INT, iarr)
gVertexArrayIndexed = None
gIndexArray = None

def main():
        global gVertexArrayIndexed, gIndexArray

        if not glfw.init():
                        return
        window = glfw.create_window(800,800,'2013011491', None,None)

        if not window:
                glfw.terminate()
                return
        glfw.make_context_current(window)
        glfw.set_drop_callback(window, drop_callback)
        glfw.set_key_callback(window, key_callback)
        glfw.swap_interval(1)

        gVertexArrayIndexed, gIndexArray = createVertexAndIndexArrayIndexed()
        count = 0
        while not glfw.window_should_close(window):
                glfw.poll_events()
                ang = count % 360
                render(ang)
                count += 1
                glfw.swap_buffers(window)
        glfw.terminate()
if __name__ == "__main__":
        main()
