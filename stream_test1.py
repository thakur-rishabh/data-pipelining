from fake_web_events import Simulation

def generate_log_line(user_count_size, session_count_day, time_to_run):
    simulation = Simulation(user_pool_size=user_count_size, sessions_per_day=session_count_day)
    events = simulation.run(duration_seconds=time_to_run)
    for event in events:
        print(event)

user_size = 1000
num_session = 15000
duration_run = 10
generate_log_line(user_size, num_session, duration_run)

