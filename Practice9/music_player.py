import pygame


pygame.init()
pygame.mixer.init()#requency=44100, size=-16, channels=2, buffer=512)

track1 = pygame.mixer.Sound("mp\Эх, Қарындас.mp3")
track2 = pygame.mixer.Sound("mp\Звезда по имени Солнце.mp3")
track3 = pygame.mixer.Sound("mp\Весна.mp3")

track_queue = [track1, track2, track3]#used for internal logic
track_names = ["Эх, Қарындас", "Звезда по имени Солнце", "Весна"] #used for display
max_tracks = len(track_names)
playing_track_num =0


running = True

is_playing = False
#P,S,N,B,Q
play_track = False
stop_track = True
next_track = False
back_track = False

screen = pygame.display.set_mode((400, 300))

def play_t():
    track_queue[playing_track_num].play()
    global play_track 
    play_track = False
    global stop_track
    stop_track = False
    global is_playing
    is_playing = True

def stop_t():
    track_queue[playing_track_num].stop()
    global is_playing
    is_playing = False

while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_track = True
            if event.key == pygame.K_s:
                stop_track = True
                play_track = False
            if event.key == pygame.K_n:
                next_track = True
            if event.key == pygame.K_b:
                back_track = True
            if event.key == pygame.K_q:
                running = False
    
    track_font = pygame.font.SysFont('arial.ttf', 25) #arial.ttf #Edwardian Script ITC
    
    if is_playing:
        p1_text = track_font.render(f' {track_names[playing_track_num]} is playing...', True, (120, 120, 200))
        screen.blit(p1_text, (0, p1_text.get_height()//2 + 10))
    else:
        p1_text = track_font.render(f' {track_names[playing_track_num]} is paused...', True, (170, 50, 50))
        screen.blit(p1_text, (0, p1_text.get_height()//2 + 10))

    play_l_font = pygame.font.SysFont('arial.ttf', 20)
    for i in range(max_tracks):
        playlist_text = play_l_font.render(f'{track_names[i]} is in playlist', True, (30,30,120))
        if i == playing_track_num:
            pygame.draw.rect(screen, (70, 70, 150), (5,p1_text.get_height() + 30 + (playlist_text.get_height() + 5)* i, (playlist_text.get_width()+5), (playlist_text.get_height() + 5)))
        screen.blit(playlist_text, (5, p1_text.get_height() + 30 + (playlist_text.get_height() + 5)* i))

    if play_track:
        play_t()
    
    if stop_track:
        stop_t()

    if next_track:
        stop_t()
        if playing_track_num == max_tracks -1:
            playing_track_num = 0 # loop around
        else:playing_track_num += 1
        next_track = False
        play_t()

    if back_track:
        stop_t()
        if playing_track_num == 0:
            playing_track_num = max_tracks-1 # loop around
        else:playing_track_num -= 1
        back_track = False
        play_t()

    #print(play_track,stop_track)

    pygame.display.flip()

