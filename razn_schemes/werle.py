def verlet_method(positions, velocities, accelerations, dt):
    new_positions = []
    for i in range(len(positions)):
        new_pos = positions[i] + velocities[i] * dt + 0.5 * accelerations[i] * dt**2
        new_positions.append(new_pos)
        velocities[i] += 0.5 * (accelerations[i] + accelerations[i]) * dt
    return new_positions, velocities