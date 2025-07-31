from vpython import *
import numpy as np

scene.title = "Underwater Drone Simulation"
scene.width = 800
scene.height = 600
scene.background = color.cyan
scene.forward = vector(-1, -0.3, -1)

g = 9.81
rho_water = 1000
mass = 10
volume = 0.007
drag_coefficient = 0.8
area = 0.04

body = cylinder(pos=vector(0, 0, 0), axis=vector(1.5, 0, 0), radius=0.25, color=color.gray(0.4))
camera = sphere(pos=body.pos + body.axis * 1.05, radius=0.15, color=color.blue, opacity=0.6)
motor_left = cylinder(pos=body.pos + vector(0.4, 0.25, 0.4), axis=vector(0, 0, 0.2), radius=0.08, color=color.red)
motor_right = cylinder(pos=body.pos + vector(0.4, -0.25, 0.4), axis=vector(0, 0, 0.2), radius=0.08, color=color.red)
stab1 = box(pos=body.pos + vector(0.5, 0.3, 0), length=0.2, height=0.05, width=0.3, color=color.white)
stab2 = box(pos=body.pos + vector(0.5, -0.3, 0), length=0.2, height=0.05, width=0.3, color=color.white)

class Drone:
    def __init__(self, body, parts):
        self.body = body
        self.parts = parts
        self.pos = body.pos

    def move(self, delta):
        self.body.pos += delta
        for part in self.parts:
            part.pos += delta
        self.pos = self.body.pos

    def set_pos(self, new_pos):
        delta = new_pos - self.body.pos
        self.move(delta)

drone = Drone(body=body, parts=[camera, motor_left, motor_right, stab1, stab2])

water = box(pos=vector(0, -15, 0), length=100, height=30, width=100, opacity=0.3, color=color.blue)
bottom = box(pos=vector(0, -30, 0), length=100, height=0.2, width=100, color=color.green)

velocity = vector(0, 0, 0)
thrust = vector(0, 0, 0)
dt = 0.01
max_bounds = 40

def get_drag(v):
    v_mag = mag(v)
    return -norm(v) * 0.5 * rho_water * v_mag**2 * drag_coefficient * area if v_mag > 0 else vector(0, 0, 0)

def key_input(evt):
    global thrust
    s = evt.key
    if s == 'w':
        thrust += vector(0, 0, -30)
    elif s == 's':
        thrust += vector(0, 0, 30)
    elif s == 'a':
        thrust += vector(-30, 0, 0)
    elif s == 'd':
        thrust += vector(30, 0, 0)
    elif s == 'r':
        thrust += vector(0, 30, 0)
    elif s == 'f':
        thrust += vector(0, -30, 0)

scene.bind('keydown', key_input)

while True:
    rate(100)
    F_gravity = vector(0, -mass * g, 0)
    F_buoyancy = vector(0, rho_water * volume * g, 0)
    F_drag = get_drag(velocity)
    F_net = F_gravity + F_buoyancy + thrust + F_drag
    acceleration = F_net / mass
    velocity += acceleration * dt
    drone.move(velocity * dt)
    thrust *= 0.9

    if drone.pos.y <= -14.5:
        velocity.y *= -0.3
        drone.set_pos(vector(drone.pos.x, -14.5, drone.pos.z))

    if abs(drone.pos.x) > max_bounds:
        velocity.x *= -0.5
        drone.set_pos(vector(np.sign(drone.pos.x) * max_bounds, drone.pos.y, drone.pos.z))

    if abs(drone.pos.z) > max_bounds:
        velocity.z *= -0.5
        drone.set_pos(vector(drone.pos.x, drone.pos.y, np.sign(drone.pos.z) * max_bounds))
