

class ScrollableText:

    def __init__(self, config, font, content="", pos_y=0):
        self.content = None
        self.font = None

        self.content_pixels_size = 0
        self.need_scrolling = False
        self.intern_step = 0
        self.text_offset = 0
        self.max_step = 0

        self.config = config
        self.set_text(content, font)
        self.pos_y = pos_y
        self.steps_calculated = False

    def increase_step(self):
        self.intern_step += 1
        if self.max_step != 0 and self.intern_step > self.max_step:
            self.intern_step = 0

    def set_step(self, step):
        self.intern_step = min(max(0, step), self.max_step)

    def will_it_change(self):
        if not self.need_scrolling:
            return False

        if self.config.pause_steps <= self.intern_step <= (self.config.pause_steps + self.text_offset) \
                or self.intern_step == self.max_step:
            return True
        return False

    def set_text(self, content, font=None):
        if font is not None:
            self.font = font

        self.content = content
        self.steps_calculated = False

    def draw_next_step(self, draw):
        self.increase_step()
        self.draw_step(draw, self.intern_step)

    def pre_calculate_scroll_metrics(self, draw):
        """
        Calculates and initializes all metrics required for horizontal text scrolling.
        """
        if self.steps_calculated:
            return

        self.content_pixels_size = int(draw.textlength(self.content, font=self.font))
        self.text_offset = self.content_pixels_size - (self.config.width - self.config.text_padding_left)

        if self.content_pixels_size > (self.config.width - self.config.text_padding_left):
            self.need_scrolling = True
            self.max_step = 2 * self.config.pause_steps + self.content_pixels_size - (self.config.width - self.config.text_padding_left)
        else:
            self.need_scrolling = False
        
        self.steps_calculated = True

    def draw_step(self, draw, step=-1):
        self.pre_calculate_scroll_metrics(draw)

        if step < 0:
            step = self.intern_step

        if not self.need_scrolling:
            draw.text(
                (self.config.width - 1, self.pos_y), 
                self.content, 
                font=self.font, 
                anchor="rm", 
                fill=self.config.primary
            )
            return

        if (step - self.config.pause_steps) > self.text_offset:
            step = self.text_offset
        else:
            if step <= self.config.pause_steps:
                step = 0
            else:
                step -= self.config.pause_steps

        draw.text(
            (self.config.width - 1 + self.text_offset - step, self.pos_y), 
            self.content, 
            font=self.font, 
            anchor="rm",
            fill=self.config.primary
        )