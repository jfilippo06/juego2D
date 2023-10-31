import pygame

start_ticks = None
countdown_seconds = None 
timer_event = pygame.USEREVENT + 1

def start_timer(duration):
    global start_ticks, countdown_seconds
    start_ticks = pygame.time.get_ticks()
    countdown_seconds = duration

def get_time():
    if start_ticks is None or countdown_seconds is None:
        return "0:00"
    total_seconds = countdown_seconds - (pygame.time.get_ticks() - start_ticks) // 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}:{seconds:02d}"

def check_timer_event():
    if start_ticks is None or countdown_seconds is None:
        return
    total_seconds = countdown_seconds - (pygame.time.get_ticks() - start_ticks) // 1000
    if total_seconds <= 0:
        pygame.event.post(pygame.event.Event(timer_event))

def stop_timer():
    global start_ticks
    start_ticks = None

def reset_timer(duration):
    stop_timer()
    start_timer(duration)
