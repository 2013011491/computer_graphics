import glfw
import numpy as np
from OpenGL.GL import *

global s
s=GL_LINE_LOOP
def render():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	glBegin(s)
	for i in range(12) :
		glVertex2f(np.cos(i/6*np.pi), np.sin(i/6*np.pi))
	glEnd()

def key_callback(window, key, scancode, action, mods):
	global s
	if key==glfw.KEY_1:
		if action==glfw.PRESS:
			s=GL_POINTS
			render()
	if key==glfw.KEY_2:
		if action==glfw.PRESS:
			s=GL_LINES
			render()
	if key==glfw.KEY_3:
		if action==glfw.PRESS:
			s=GL_LINE_STRIP
			render()
	if key==glfw.KEY_4:
		if action==glfw.PRESS:
			s=GL_LINE_LOOP
			render()
	if key==glfw.KEY_5:
		if action==glfw.PRESS:
			s=GL_TRIANGLES
			render()
	if key==glfw.KEY_6:
		if action==glfw.PRESS:
			s=GL_TRIANGLE_STRIP
			render()
	if key==glfw.KEY_7:
		if action==glfw.PRESS:
			s=GL_TRIANGLE_FAN
			render()
	if key==glfw.KEY_8:
		if action==glfw.PRESS:
			s=GL_QUADS
			render()
	if key==glfw.KEY_9:
		if action==glfw.PRESS:
			s=GL_QUAD_STRIP
			render()
	if key==glfw.KEY_0:
		if action==glfw.PRESS:
			s=GL_POLYGON
			render()
	elif key==glfw.KEY_SPACE and action==glfw.PRESS:
		print ('press space: (%d, %d)'%glfw.get_cursor_pos(window))

def main():
	if not glfw.init():
		return
	window = glfw.create_window(480,480,"Hello World",None,None)
	if not window :
		glfw.terminate()
		return
	glfw.set_key_callback(window, key_callback)
# Make the window's context current
	glfw.make_context_current(window)
# Loop until the user closes the window
	while not glfw.window_should_close(window):
# Poll events
		glfw.poll_events()
# Render here, e.g. using pyOpenGL
		render()
# Swap front and back buffers
		glfw.swap_buffers(window)
	glfw.terminate()
if __name__ == "__main__":
	main()