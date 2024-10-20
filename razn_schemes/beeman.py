
def beeman_method(positions, velocities, accelerations, prev_accelerations, dt):
    new_positions = []
    new_velocities = []
    for i in range(len(positions)):
        new_pos = positions[i] + velocities[i] * dt + (4/6) * accelerations[i] * dt**2 - (1/6) * prev_accelerations[i] * dt**2
        new_positions.append(new_pos)
        new_vel = velocities[i] + (2/3) * accelerations[i] * dt - (1/3) * prev_accelerations[i] * dt
        new_velocities.append(new_vel)
    return new_positions, new_velocities