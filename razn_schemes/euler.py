
def euler_method(positions, velocities, accelerations, dt):
    for i in range(len(positions)):
        velocities[i] += accelerations[i] * dt
        positions[i] += velocities[i] * dt
    return positions, velocities