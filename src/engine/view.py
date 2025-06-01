import pygame


class View:

    def __init__(self, width: int, height: int, x: int = 0, y: int = 0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y


class Image(View):

    def __init__(self,
                 url: str,
                 width: int,
                 height: int,
                 x: int = 0,
                 y: int = 0):
        super().__init__(width, height, x, y)
        self.url = url
        img = pygame.image.load(url)
        self.view = pygame.transform.scale(img, (width, height))

    def get_view(self):
        return self.view


class Animation(View):

    def __init__(self,
                 frames: list[View],
                 duration: int,
                 width: int,
                 height: int,
                 x: int = 0,
                 y: int = 0):
        super().__init__(width, height, x, y)
        self.frames = frames
        self.duration = duration
        self.current_frame = 0
        self.elapsed_time = 0

    def get_current_frame(self):
        return self.frames[self.current_frame]

    def get_view(self):
        return self.get_current_frame().get_view()

    def update(self, delta_time):
        self.elapsed_time += delta_time
        if self.elapsed_time >= self.duration:
            self.elapsed_time = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
