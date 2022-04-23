import pymunk
import pymunk.pygame_util
from pymunk import Vec2d
import numpy as np
import pygame

class Drone():

    def __init__(self, x, y, angle, height, width, mass_f, mass_l, mass_r, space):
        distance_between_joints = height/2 - 3
        self.drone_radius = width/2 - height/2

        #Drone's frame properties
        self.frame_shape = pymunk.Poly.create_box(None, size=(width, height/2))
        frame_moment_of_inertia = pymunk.moment_for_poly(mass_f, self.frame_shape.get_vertices())

        frame_body = pymunk.Body(mass_f, frame_moment_of_inertia, body_type=pymunk.Body.DYNAMIC)
        frame_body.position = x, y
        frame_body.angle = angle

        self.frame_shape.body = frame_body
        self.frame_shape.sensor = True
        self.frame_shape.color = pygame.Color((66, 135, 245))

        space.add(frame_body, self.frame_shape)

        #Drone's left motor properties
        self.left_motor_shape = pymunk.Poly.create_box(None, size=(height, height))
        left_motor_moment_of_inertia = pymunk.moment_for_poly(mass_l, self.left_motor_shape.get_vertices())

        left_motor_body = pymunk.Body(mass_l, left_motor_moment_of_inertia, body_type=pymunk.Body.DYNAMIC)
        left_motor_body.position = np.cos(angle+np.pi)*self.drone_radius+x, np.sin(angle+np.pi)*self.drone_radius+y
        left_motor_body.angle = angle

        self.left_motor_shape.body = left_motor_body
        self.left_motor_shape.sensor = True
        self.left_motor_shape.color = pygame.Color((33, 93, 191))

        space.add(left_motor_body, self.left_motor_shape)

        #Drone's right motor properties
        self.right_motor_shape = pymunk.Poly.create_box(None, size=(height, height))
        right_motor_moment_of_inertia = pymunk.moment_for_poly(mass_r, self.right_motor_shape.get_vertices())

        right_motor_body = pymunk.Body(mass_r, right_motor_moment_of_inertia, body_type=pymunk.Body.DYNAMIC)
        right_motor_body.position = np.cos(angle)*self.drone_radius+x, np.sin(angle)*self.drone_radius+y
        right_motor_body.angle = angle

        self.right_motor_shape.body = right_motor_body
        self.right_motor_shape.sensor = True
        self.right_motor_shape.color = pygame.Color((33, 93, 191))

        space.add(right_motor_body, self.right_motor_shape)

        #Properties of the joints
        motor_point = (-distance_between_joints, 0)
        frame_point = (-self.drone_radius - distance_between_joints, 0)
        self.left_1 = pymunk.PivotJoint(self.left_motor_shape.body, self.frame_shape.body, motor_point, frame_point)
        self.left_1.error_bias = 0
        space.add(self.left_1)

        motor_point = (0, 0)
        frame_point = (-self.drone_radius, 0)
        self.left_2 = pymunk.PivotJoint(self.left_motor_shape.body, self.frame_shape.body, motor_point, frame_point)
        self.left_2.error_bias = 0
        space.add(self.left_2)

        motor_point = (distance_between_joints, 0)
        frame_point = (-self.drone_radius + distance_between_joints, 0)
        self.left_3 = pymunk.PivotJoint(self.left_motor_shape.body, self.frame_shape.body, motor_point, frame_point)
        self.left_3.error_bias = 0
        space.add(self.left_3)

        motor_point = (-distance_between_joints, 0)
        frame_point = (self.drone_radius - distance_between_joints, 0)
        self.right_1 = pymunk.PivotJoint(self.right_motor_shape.body, self.frame_shape.body, motor_point, frame_point)
        self.right_1.error_bias = 0
        space.add(self.right_1)

        motor_point = (0, 0)
        frame_point = (self.drone_radius, 0)
        self.right_2 = pymunk.PivotJoint(self.right_motor_shape.body, self.frame_shape.body, motor_point, frame_point)
        self.right_2.error_bias = 0
        space.add(self.right_2)

        motor_point = (distance_between_joints, 0)
        frame_point = (self.drone_radius + distance_between_joints, 0)
        self.right_3 = pymunk.PivotJoint(self.right_motor_shape.body, self.frame_shape.body, motor_point, frame_point)
        self.right_3.error_bias = 0
        space.add(self.right_3)

    def change_positions(self, x, y, space):
        self.frame_shape.body.position = x, y
        space.reindex_shapes_for_body(self.frame_shape.body)

        angle = self.frame_shape.body.angle

        self.left_motor_shape.body.position = np.cos(angle+np.pi)*self.drone_radius+x, np.sin(angle+np.pi)*self.drone_radius+y
        space.reindex_shapes_for_body(self.left_motor_shape.body)

        self.right_motor_shape.body.position = np.cos(angle)*self.drone_radius+x, np.sin(angle)*self.drone_radius+y
        space.reindex_shapes_for_body(self.right_motor_shape.body)
