#!/usr/bin/env python3
import struct
import hashlib


import struct
import random
import hashlib

def generateByteString():
    execution_flag = random.choice([0, 1])

    motor_values = [random.uniform(-100, 100) for _ in range(4)]  # Random floats between -10 and 10
    motor_values_bytes = struct.pack('4f', *motor_values)

    actuator_direction = random.choice([1, 2])
    actuator_direction_bytes = struct.pack('B', actuator_direction)

    actuator_current_value = random.uniform(0, 10)
    actuator_current_value_bytes = struct.pack('d', actuator_current_value)

    ultrasound_values_length = random.randint(1, 15)
    ultrasound_values = [random.uniform(0, 10) for _ in range(ultrasound_values_length)]  # Random floats between 0 and 5
    ultrasound_values_bytes = b''.join(struct.pack('d', val) for val in ultrasound_values)

    ultrasound_start_flag = b'USTR'
    ultrasound_end_flag = b'UEND'

    led_status = random.choice([0, 1])
    led_status_bytes = struct.pack('B', led_status)

    pre_hash_bytes = (struct.pack('B', execution_flag) +
                      motor_values_bytes +
                      actuator_direction_bytes +
                      actuator_current_value_bytes +
                      ultrasound_start_flag +
                      ultrasound_values_bytes +
                      ultrasound_end_flag +
                      led_status_bytes)

    hash_value = hashlib.sha256(pre_hash_bytes).digest()

    null_terminator = b'TERM'

    final_byte_string = pre_hash_bytes + hash_value + null_terminator

    with open('../robot_data.bin', 'wb') as file:
        file.write(final_byte_string)

generateByteString()