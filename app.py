from flask import Flask, render_template, request, jsonify, session
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
app.secret_key = 'ep_virtual_lab_kmit'

laser_current=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.4000000000000001, 0.4333333333333333, 0.5, 0.6, 0.6999999999999998, 0.8000000000000002, 1.0, 1.3, 1.566666666666667, 2.033333333333333, 2.366666666666667, 3.1, 3.5, 4.133333333333333, 5.2, 5.7, 7.033333333333334, 7.833333333333333, 8.966666666666667, 10.46666666666667, 11.46666666666667, 13.0, 14.86666666666667, 15.76666666666667, 17.36666666666666, 19.4, 21.0]
laser_voltage=[0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.1, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18, 1.19, 1.2, 1.21, 1.22, 1.23, 1.24, 1.25, 1.26, 1.27, 1.28, 1.29, 1.3, 1.31, 1.32, 1.33, 1.34, 1.35, 1.36, 1.37, 1.38, 1.39, 1.4, 1.41, 1.42, 1.43, 1.44, 1.45, 1.46, 1.47, 1.48, 1.49, 1.5, 1.51, 1.52, 1.53, 1.54, 1.55, 1.56, 1.57, 1.58, 1.59, 1.6, 1.61, 1.62, 1.63, 1.64, 1.65, 1.66, 1.67, 1.68, 1.69, 1.7, 1.71, 1.72, 1.73, 1.74, 1.75, 1.76, 1.77, 1.78, 1.79, 1.8, 1.81, 1.82, 1.83, 1.84, 1.85, 1.86, 1.87, 1.88, 1.89, 1.9, 1.91, 1.92, 1.93, 1.94, 1.95, 1.96, 1.97, 1.98, 1.99, 2.0]
laser_dict={0.0: 0.0, 0.01: 0.0, 0.02: 0.0, 0.03: 0.0, 0.04: 0.0, 0.05: 0.0, 0.06: 0.0, 0.07: 0.0, 0.08: 0.0, 0.09: 0.0, 0.1: 0.0, 0.11: 0.0, 0.12: 0.0, 0.13: 0.0, 0.14: 0.0, 0.15: 0.0, 0.16: 0.0, 0.17: 0.0, 0.18: 0.0, 0.19: 0.0, 0.2: 0.0, 0.21: 0.0, 0.22: 0.0, 0.23: 0.0, 0.24: 0.0, 0.25: 0.0, 0.26: 0.0, 0.27: 0.0, 0.28: 0.0, 0.29: 0.0, 0.3: 0.0, 0.31: 0.0, 0.32: 0.0, 0.33: 0.0, 0.34: 0.0, 0.35: 0.0, 0.36: 0.0, 0.37: 0.0, 0.38: 0.0, 0.39: 0.0, 0.4: 0.0, 0.41: 0.0, 0.42: 0.0, 0.43: 0.0, 0.44: 0.0, 0.45: 0.0, 0.46: 0.0, 0.47: 0.0, 0.48: 0.0, 0.49: 0.0, 0.5: 0.0, 0.51: 0.0, 0.52: 0.0, 0.53: 0.0, 0.54: 0.0, 0.55: 0.0, 0.56: 0.0, 0.57: 0.0, 0.58: 0.0, 0.59: 0.0, 0.6: 0.0, 0.61: 0.0, 0.62: 0.0, 0.63: 0.0, 0.64: 0.0, 0.65: 0.0, 0.66: 0.0, 0.67: 0.0, 0.68: 0.0, 0.69: 0.0, 0.7: 0.0, 0.71: 0.0, 0.72: 0.0, 0.73: 0.0, 0.74: 0.0, 0.75: 0.0, 0.76: 0.0, 0.77: 0.0, 0.78: 0.0, 0.79: 0.0, 0.8: 0.0, 0.81: 0.0, 0.82: 0.0, 0.83: 0.0, 0.84: 0.0, 0.85: 0.0, 0.86: 0.0, 0.87: 0.0, 0.88: 0.0, 0.89: 0.0, 0.9: 0.0, 0.91: 0.0, 0.92: 0.0, 0.93: 0.0, 0.94: 0.0, 0.95: 0.0, 0.96: 0.0, 0.97: 0.0, 0.98: 0.0, 0.99: 0.0, 1.0: 0.0, 1.01: 0.0, 1.02: 0.0, 1.03: 0.0, 1.04: 0.0, 1.05: 0.0, 1.06: 0.0, 1.07: 0.0, 1.08: 0.0, 1.09: 0.0, 1.1: 0.0, 1.11: 0.0, 1.12: 0.0, 1.13: 0.0, 1.14: 0.0, 1.15: 0.0, 1.16: 0.0, 1.17: 0.0, 1.18: 0.0, 1.19: 0.0, 1.2: 0.0, 1.21: 0.0, 1.22: 0.0, 1.23: 0.0, 1.24: 0.0, 1.25: 0.0, 1.26: 0.0, 1.27: 0.0, 1.28: 0.0, 1.29: 0.0, 1.3: 0.0, 1.31: 0.0, 1.32: 0.0, 1.33: 0.0, 1.34: 0.0, 1.35: 0.0, 1.36: 0.0, 1.37: 0.0, 1.38: 0.0, 1.39: 0.0, 1.4: 0.0, 1.41: 0.0, 1.42: 0.0, 1.43: 0.0, 1.44: 0.0, 1.45: 0.0, 1.46: 0.0, 1.47: 0.0, 1.48: 0.0, 1.49: 0.0, 1.5: 0.0, 1.51: 0.0, 1.52: 0.0, 1.53: 0.0, 1.54: 0.0, 1.55: 0.0, 1.56: 0.0, 1.57: 0.0, 1.58: 0.0, 1.59: 0.0, 1.6: 0.0, 1.61: 0.0, 1.62: 0.0, 1.63: 0.0, 1.64: 0.0, 1.65: 0.0, 1.66: 0.0, 1.67: 0.2, 1.68: 0.2, 1.69: 0.2, 1.7: 0.2, 1.71: 0.3, 1.72: 0.3, 1.73: 0.3, 1.74: 0.4000000000000001, 1.75: 0.4333333333333333, 1.76: 0.5, 1.77: 0.6, 1.78: 0.6999999999999998, 1.79: 0.8000000000000002, 1.8: 1.0, 1.81: 1.3, 1.82: 1.566666666666667, 1.83: 2.033333333333333, 1.84: 2.366666666666667, 1.85: 3.1, 1.86: 3.5, 1.87: 4.133333333333333, 1.88: 5.2, 1.89: 5.7, 1.9: 7.033333333333334, 1.91: 7.833333333333333, 1.92: 8.966666666666667, 1.93: 10.46666666666667, 1.94: 11.46666666666667, 1.95: 13.0, 1.96: 14.86666666666667, 1.97: 15.76666666666667, 1.98: 17.36666666666666, 1.99: 19.4, 2.0: 21.0}
led_current=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06666666666666667, 0.06666666666666667, 0.1, 0.1333333333333333, 0.1333333333333333, 0.1333333333333333, 0.1333333333333333, 0.1333333333333333, 0.1666666666666667, 0.2333333333333333, 0.2666666666666667, 0.3333333333333333, 0.36666666666667, 0.4666666666666666, 0.5666666666666667, 0.6999999999999998, 0.8666666666666667, 1.066666666666667, 1.4, 1.7, 2.133333333333333, 2.6, 3.2, 3.833333333333333, 4.566666666666667, 5.5, 6.333333333333333, 7.133333333333333, 8.166666666666666, 9.200000000000001, 10.3, 11.46666666666667, 12.53333333333333, 13.86666666666667, 15.0, 16.36666666666667, 17.7, 19.13333333333333, 20.2, 21.76666666666667, 22.83333333333333, 24.43333333333333, 25.0]
led_voltage=[0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.1, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18, 1.19, 1.2, 1.21, 1.22, 1.23, 1.24, 1.25, 1.26, 1.27, 1.28, 1.29, 1.3, 1.31, 1.32, 1.33, 1.34, 1.35, 1.36, 1.37, 1.38, 1.39, 1.4, 1.41, 1.42, 1.43, 1.44, 1.45, 1.46, 1.47, 1.48, 1.49, 1.5, 1.51, 1.52, 1.53, 1.54, 1.55, 1.56, 1.57, 1.58, 1.59, 1.6, 1.61, 1.62, 1.63, 1.64, 1.65, 1.66, 1.67, 1.68, 1.69, 1.7, 1.71, 1.72, 1.73, 1.74, 1.75, 1.76, 1.77, 1.78, 1.79, 1.8, 1.81, 1.82, 1.83, 1.84, 1.85, 1.86, 1.87, 1.88, 1.89, 1.9, 1.91, 1.92, 1.93, 1.94, 1.95, 1.96, 1.97, 1.98]
led_intensity=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3333333333333333, 0.3333333333333333, 0.6666666666666666, 1.0, 1.0, 1.0, 1.0, 1.0, 1.666666666666667, 2.333333333333333, 2.333333333333333, 2.333333333333333, 2.333333333333333, 2.333333333333333, 123.6666666666667, 604.6666666666666, 629.6666666666666, 642.3333333333334, 654.0, 660.3333333333334, 667.0, 672.0, 677.3333333333334, 682.3333333333334, 687.0, 691.3333333333334, 694.6666666666666, 698.0, 700.6666666666666, 703.6666666666666, 706.0, 709.0, 710.3333333333334, 712.6666666666666, 714.3333333333334, 716.3333333333334, 718.3333333333334, 720.0, 721.0, 722.6666666666666, 724.3333333333334, 725.3333333333334, 726.3333333333334]
led_dict={0.0: (0.0, 0.0), 0.01: (0.0, 0.0), 0.02: (0.0, 0.0), 0.03: (0.0, 0.0), 0.04: (0.0, 0.0), 0.05: (0.0, 0.0), 0.06: (0.0, 0.0), 0.07: (0.0, 0.0), 0.08: (0.0, 0.0), 0.09: (0.0, 0.0), 0.1: (0.0, 0.0), 0.11: (0.0, 0.0), 0.12: (0.0, 0.0), 0.13: (0.0, 0.0), 0.14: (0.0, 0.0), 0.15: (0.0, 0.0), 0.16: (0.0, 0.0), 0.17: (0.0, 0.0), 0.18: (0.0, 0.0), 0.19: (0.0, 0.0), 0.2: (0.0, 0.0), 0.21: (0.0, 0.0), 0.22: (0.0, 0.0), 0.23: (0.0, 0.0), 0.24: (0.0, 0.0), 0.25: (0.0, 0.0), 0.26: (0.0, 0.0), 0.27: (0.0, 0.0), 0.28: (0.0, 0.0), 0.29: (0.0, 0.0), 0.3: (0.0, 0.0), 0.31: (0.0, 0.0), 0.32: (0.0, 0.0), 0.33: (0.0, 0.0), 0.34: (0.0, 0.0), 0.35: (0.0, 0.0), 0.36: (0.0, 0.0), 0.37: (0.0, 0.0), 0.38: (0.0, 0.0), 0.39: (0.0, 0.0), 0.4: (0.0, 0.0), 0.41: (0.0, 0.0), 0.42: (0.0, 0.0), 0.43: (0.0, 0.0), 0.44: (0.0, 0.0), 0.45: (0.0, 0.0), 0.46: (0.0, 0.0), 0.47: (0.0, 0.0), 0.48: (0.0, 0.0), 0.49: (0.0, 0.0), 0.5: (0.0, 0.0), 0.51: (0.0, 0.0), 0.52: (0.0, 0.0), 0.53: (0.0, 0.0), 0.54: (0.0, 0.0), 0.55: (0.0, 0.0), 0.56: (0.0, 0.0), 0.57: (0.0, 0.0), 0.58: (0.0, 0.0), 0.59: (0.0, 0.0), 0.6: (0.0, 0.0), 0.61: (0.0, 0.0), 0.62: (0.0, 0.0), 0.63: (0.0, 0.0), 0.64: (0.0, 0.0), 0.65: (0.0, 0.0), 0.66: (0.0, 0.0), 0.67: (0.0, 0.0), 0.68: (0.0, 0.0), 0.69: (0.0, 0.0), 0.7: (0.0, 0.0), 0.71: (0.0, 0.0), 0.72: (0.0, 0.0), 0.73: (0.0, 0.0), 0.74: (0.0, 0.0), 0.75: (0.0, 0.0), 0.76: (0.0, 0.0), 0.77: (0.0, 0.0), 0.78: (0.0, 0.0), 0.79: (0.0, 0.0), 0.8: (0.0, 0.0), 0.81: (0.0, 0.0), 0.82: (0.0, 0.0), 0.83: (0.0, 0.0), 0.84: (0.0, 0.0), 0.85: (0.0, 0.0), 0.86: (0.0, 0.0), 0.87: (0.0, 0.0), 0.88: (0.0, 0.0), 0.89: (0.0, 0.0), 0.9: (0.0, 0.0), 0.91: (0.0, 0.0), 0.92: (0.0, 0.0), 0.93: (0.0, 0.0), 0.94: (0.0, 0.0), 0.95: (0.0, 0.0), 0.96: (0.0, 0.0), 0.97: (0.0, 0.0), 0.98: (0.0, 0.0), 0.99: (0.0, 0.0), 1.0: (0.0, 0.0), 1.01: (0.0, 0.0), 1.02: (0.0, 0.0), 1.03: (0.0, 0.0), 1.04: (0.0, 0.0), 1.05: (0.0, 0.0), 1.06: (0.0, 0.0), 1.07: (0.0, 0.0), 1.08: (0.0, 0.0), 1.09: (0.0, 0.0), 1.1: (0.0, 0.0), 1.11: (0.0, 0.0), 1.12: (0.0, 0.0), 1.13: (0.0, 0.0), 1.14: (0.0, 0.0), 1.15: (0.0, 0.0), 1.16: (0.0, 0.0), 1.17: (0.0, 0.0), 1.18: (0.0, 0.0), 1.19: (0.0, 0.0), 1.2: (0.0, 0.0), 1.21: (0.0, 0.0), 1.22: (0.0, 0.0), 1.23: (0.0, 0.0), 1.24: (0.0, 0.0), 1.25: (0.0, 0.0), 1.26: (0.0, 0.0), 1.27: (0.0, 0.0), 1.28: (0.0, 0.0), 1.29: (0.0, 0.0), 1.3: (0.0, 0.0), 1.31: (0.0, 0.0), 1.32: (0.0, 0.0), 1.33: (0.0, 0.0), 1.34: (0.0, 0.0), 1.35: (0.0, 0.0), 1.36: (0.0, 0.0), 1.37: (0.0, 0.0), 1.38: (0.0, 0.0), 1.39: (0.0, 0.0), 1.4: (0.0, 0.0), 1.41: (0.0, 0.0), 1.42: (0.0, 0.0), 1.43: (0.0, 0.0), 1.44: (0.0, 0.0), 1.45: (0.0, 0.0), 1.46: (0.0, 0.0), 1.47: (0.0, 0.0), 1.48: (0.0, 0.0), 1.49: (0.0, 0.0), 1.5: (0.0, 0.0), 1.51: (0.0, 0.0), 1.52: (0.0, 0.0), 1.53: (0.0, 0.0), 1.54: (0.0, 0.0), 1.55: (0.0, 0.0), 1.56: (0.06666666666666667, 0.3333333333333333), 1.57: (0.06666666666666667, 0.3333333333333333), 1.58: (0.1, 0.6666666666666666), 1.59: (0.1333333333333333, 1.0), 1.6: (0.1333333333333333, 1.0), 1.61: (0.1333333333333333, 1.0), 1.62: (0.1333333333333333, 1.0), 1.63: (0.1333333333333333, 1.0), 1.64: (0.1666666666666667, 1.666666666666667), 1.65: (0.2333333333333333, 2.333333333333333), 1.66: (0.2666666666666667, 2.333333333333333), 1.67: (0.3333333333333333, 2.333333333333333), 1.68: (0.36666666666667, 2.333333333333333), 1.69: (0.4666666666666666, 2.333333333333333), 1.7: (0.5666666666666667, 123.6666666666667), 1.71: (0.6999999999999998, 604.6666666666666), 1.72: (0.8666666666666667, 629.6666666666666), 1.73: (1.066666666666667, 642.3333333333334), 1.74: (1.4, 654.0), 1.75: (1.7, 660.3333333333334), 1.76: (2.133333333333333, 667.0), 1.77: (2.6, 672.0), 1.78: (3.2, 677.3333333333334), 1.79: (3.833333333333333, 682.3333333333334), 1.8: (4.566666666666667, 687.0), 1.81: (5.5, 691.3333333333334), 1.82: (6.333333333333333, 694.6666666666666), 1.83: (7.133333333333333, 698.0), 1.84: (8.166666666666666, 700.6666666666666), 1.85: (9.200000000000001, 703.6666666666666), 1.86: (10.3, 706.0), 1.87: (11.46666666666667, 709.0), 1.88: (12.53333333333333, 710.3333333333334), 1.89: (13.86666666666667, 712.6666666666666), 1.9: (15.0, 714.3333333333334), 1.91: (16.36666666666667, 716.3333333333334), 1.92: (17.7, 718.3333333333334), 1.93: (19.13333333333333, 720.0), 1.94: (20.2, 721.0), 1.95: (21.76666666666667, 722.6666666666666), 1.96: (22.83333333333333, 724.3333333333334), 1.97: (24.43333333333333, 725.3333333333334), 1.98: (25.0, 726.3333333333334)}


light = {1.5: [0.07, 0.1, 0.13, 0.17, 0.23, 0.27], 1.9: [0.33, 0.37, 0.47, 0.57], 2: [0.7, 0.87, 1.07, 1.4],
         2.8: [1.7, 2.13, 2.6],
         3.4: [3.2, 3.83, 4.57], 3.7: [5.5, 6.33, 7.13], 4.3: [7.03, 7.83, 8.17], 4.6: [9.2, 10.2, 11.47],
         5: [12.53, 13.87],
         5.3: [15, 16.37, 17.7], 6: [19.13, 20.2, 21.77, 22.83], 6.5: [24.43, 25]}

def generate_graph(page, title, d, x_vals, y_vals, li_vi):

    plt.plot(x_vals, y_vals, color='black', marker='o', markersize=0)

    x, y = [], []
    for v in session['voltages']:
        if page == 'laser_sim.html':
            x, y = v, d[v]
        elif page == 'led_vi.html':
            x, y = v, d[v][0]
        elif page == 'led_li.html':
            x, y = d[v][0], d[v][1]
        plt.plot(x, y, color='blue', marker='o', markerfacecolor='blue', markersize=5)


    if page == 'led_li.html':
        plt.xlabel('Current(mA)')
        plt.ylabel('Light Intensity(mCd)')
    else:
        plt.xlabel('Voltage (V)')
        plt.ylabel('Current (mA)')
    plt.title(li_vi + ' characteristics of ' + title)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    return plot_base64



def processVI(page, title, d, x_vals, y_vals, li_vi):
    """
        Parameters are same as generate_graph() reason being....
        If the Generate Graph button is clicked these parameters are passed to generate_graph()
        To avoid confusion, the variables names are same, however these are local variables to this function.
    """
    graph = request.form.get('VIgraph')
    # Checking whether Generate Graph is clicked or not, returns None if not clicked
    l = len(session['voltages'])
    if graph:
        g = generate_graph(page, title, d, x_vals, y_vals, li_vi)
        return render_template(page, graph=graph, length=l, table=session['table'], current=0.0, voltage=0.0,
                               height=1.5, color='white', g=g)
    else:
        session['voltage'] = float(request.form['voltage'])
        if page == 'laser_sim.html':
            session['current'] = round(d[session['voltage']], 2)
        elif page == 'led_vi.html':
            session['current'] = round(d[session['voltage']][0], 2)
        if [session['voltage'], session['current']] not in session['table'].values():
            session['voltages'].append(session['voltage'])
            session['table'][str(len(session['voltages']) - 1)] = [session['voltage'], session['current']]
        else:
            return render_template(page, graph=graph, length=l, table=session['table'], current=0.0, voltage=0.0,
                                   height=1.5, color='white', flag=1)
        if session['current'] == 0:
            return render_template(page, current=session['current'], voltage=session['voltage'], height=1.5,
                                   color='white',
                                   table=session['table'], graph=None, length=l)
        else:
            if page == 'laser_sim.html':
                return render_template(page, current=session['current'], voltage=session['voltage'], height=3,
                                       color='red',
                                       table=session['table'], graph=None, length=l)
            for i in light:
                if session['current'] in light[i]:
                    height = i
                    return render_template(page, current=session['current'], voltage=session['voltage'], height=height,
                                           color='red', table=session['table'], graph=None, length=l)


def led_init():
    # These values must be initialised whenever the page is reloaded for LED VI and LI
    # Hence this function...

    session['voltages'] = []
    session['table'] = {i: ['', ''] for i in range(8)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/laser_theory')
def lasertheory():
    return render_template('laser_theory.html')


@app.route('/laser_sim')
def lasersim():
    # Initialising variables for Laser simulation similar to led_init()
    session['voltages'] = []
    session['table'] = {}
    for i in range(8):
        session['table'][i] = ['', '']
    return render_template('laser_sim.html', current=0.00, voltage=0.00, height=1.5, color='white',
                           table=session['table'],
                           graph=None, length=0)


@app.route('/laser_viva')
def laserviva():
    return render_template('laser_viva.html')


@app.route('/led_theory')
def ledtheory():
    return render_template('led_theory.html')


@app.route('/led_viva')
def ledviva():
    return render_template('led_viva.html')


@app.route('/led_vi')
def ledsimVI():
    led_init()
    return render_template('led_vi.html', current=0.00, voltage=0.00, height=1.5, color='white', table=session['table'],
                           length=0,
                           graph=None)


@app.route('/led_li')
def ledsimLI():
    led_init()
    return render_template('led_li.html', current=0.00, voltage=0.00, height=1.5, color='white', table=session['table'],
                           length=0,
                           graph=None)

@app.route('/process_form_laser', methods=['POST'])
def process_form_laser():
    return processVI('laser_sim.html', 'Laser Diode', laser_dict, laser_voltage, laser_current, 'VI')

@app.route('/process_form_ledVI', methods=['POST'])
def process_form_ledVI():
    return processVI('led_vi.html', 'LED', led_dict, led_voltage, led_current, 'VI')


@app.route('/process_form_ledLI', methods=['POST'])
def process_form_ledLI():
    graph = request.form.get('VIgraph')
    l = len(session['voltages'])
    if graph:
        g = generate_graph('led_li.html', 'LED', led_dict, led_current, led_intensity, 'LI')
        return render_template('led_li.html', graph=graph, length=l, table=session['table'], g=g)
    else:
        session['voltage'] = float(request.form['voltage'])
        session['current'] = round(led_dict[session['voltage']][0], 2)
        session['intensity'] = round(led_dict[session['voltage']][1])
        if session['voltage'] not in session['voltages']:
            session['voltages'].append(session['voltage'])
            session['table'][str(len(session['voltages']) - 1)] = [session['intensity'], session['current']]
        else:
            return render_template('led_li.html', graph=graph, length=l, table=session['table'], current=0.0,
                                   voltage=0.0, height=1.5,
                                   color='white', flag=1)
        if session['current'] == 0:
            return render_template('led_li.html', current=session['current'], voltage=session['intensity'], height=1.5,
                                   color='white',
                                   table=session['table'], graph=None, length=l)
        else:
            for i in light:
                if session['current'] in light[i]:
                    height = i
                    return render_template('led_li.html', current=session['current'], voltage=session['intensity'],
                                           height=height,
                                           color='red', table=session['table'], graph=None, length=l)


blue = [round(i * 10 ** -2, 2) for i in range(99, -1, -1)]
green = [round(i * 10 ** -2, 2) for i in range(72, -1, -1)]
orange = [round(i * 10 ** -2, 2) for i in range(42, -1, -1)]
red = [round(i * 10 ** -2, 2) for i in range(18, -1, -1)]
v = [round(-i * 10 ** -2, 2) for i in range(0, 101)]


def photocurrent(voltage):
    pcurrent = 0.0
    try:
        if light_off:
            pcurrent = 0.0
        elif voltage == 0 and light_clicked:
            if session['color'] == 'red':
                pcurrent = red[0]
            elif session['color'] == 'green':
                pcurrent = green[0]
            elif session['color'] == 'blue':
                pcurrent = blue[0]
            elif session['color'] == 'orange':
                pcurrent = orange[0]
        else:
            if session['color'] == 'red':
                if v.index(round(voltage, 2)) > len(red) - 1:
                    pcurrent = 0
                else:
                    pcurrent = red[v.index(round(voltage, 2))]
            elif session['color'] == 'green':
                if v.index(round(voltage, 2)) > len(green) - 1:
                    pcurrent = 0
                else:
                    pcurrent = green[v.index(round(voltage, 2))]
            elif session['color'] == 'blue':
                if v.index(round(voltage, 2)) > len(blue) - 1:
                    pcurrent = 0
                else:
                    pcurrent = blue[v.index(round(voltage, 2))]
            elif session['color'] == 'orange':
                if v.index(round(voltage, 2)) > len(orange) - 1:
                    pcurrent = 0
                else:
                    pcurrent = orange[v.index(round(voltage, 2))]
            else:
                pcurrent = 0
    except NameError:
        pcurrent = 0
    return pcurrent


@app.route('/photo_sim')
def photosim():
    session['S_potential'] = ['' for i in range(4)]
    session['voltage'] = request.args.get("voltage", default=0.0, type=float)
    current = 0.0
    return render_template('photo_sim.html', voltage=session['voltage'], current=current, list=session['S_potential'], graph=None, color=None)


@app.route('/update_values', methods=['POST'])
def update_values():
    session['volts'] = request.form.get('voltage', type=float)
    session['pcurrent'] = photocurrent(session['volts'])
    response = {'voltage': session['volts'], 'current': session['pcurrent']}
    return jsonify(response)


@app.route('/process_form_photo', methods=['POST'])
def process_form_photo():
    global light_clicked, light_off
    graph = request.form.get('graph')
    light_off = 1
    session['voltage'] = request.args.get("voltage", default=0.0, type=float)
    light_clicked = request.form.get('submit-color')
    light_off = request.form.get('off')
    session['color'] = request.form['Color of Light']
    if graph and '' in session['S_potential']:
        session['color']='none'
        return render_template('photo_sim.html', lightBtn=light_clicked, lightOFF=light_off, color=session['color'], voltage=0.0,
                        current=0.0, list=session['S_potential'], graph=graph)
    else:
        session['pcurrent'] = photocurrent(session['voltage'])
        return render_template('photo_sim.html', lightBtn=light_clicked, lightOFF=light_off, color=session['color'], voltage=session['voltage'],
                           current=session['pcurrent'], list=session['S_potential'], graph=graph)


@app.route('/process_photo_voltage', methods=['POST'])
def process_photo_voltage():
    flag=1
    submit_clicked = request.form.get('submit-voltage')
    if submit_clicked:
        try:
            session['pcurrent'] = photocurrent(session['volts'])
            if session['color'] == 'red' and session['volts'] == -0.18:
                session['S_potential'][0] = abs(session['volts'])
                flag=0
            elif session['color'] == 'green' and session['volts'] == -0.72:
                session['S_potential'][1] = abs(session['volts'])
                flag=0
            elif session['color'] == 'blue' and session['volts'] == -0.99:
                session['S_potential'][2] = abs(session['volts'])
                flag=0
            elif session['color'] == 'orange' and session['volts'] == -0.42:
                session['S_potential'][3] = abs(session['volts'])
                flag=0
            elif session['color'] == 'none':
                return render_template('photo_sim.html', lightBtn=0,voltage=0.0, current=0.0, list=session['S_potential'], graph=None, lightError=1)
        except KeyError:
            return render_template('photo_sim.html', lightBtn=0, voltage=0.0, current=0.0, list=session['S_potential'], graph=None,
                                   lightError=1)
        return render_template('photo_sim.html', lightBtn=1, color=session['color'], voltage=session['volts'], current=session['pcurrent'],
                           list=session['S_potential'], graph=None, flag=flag)


@app.route('/photo_theory')
def phototheory():
    return render_template('photo_theory.html')

@app.route('/photo_viva')
def photoviva():
    return render_template('photo_viva.html')

if __name__ == '__main__':
    app.run()
