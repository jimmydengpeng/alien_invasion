class Settings:

    def __init__(self):
        # static settings:
        self.screen_width = 1200  # 1200
        self.screen_height = 800  # 800
        self.bg_color = (230, 230, 230)
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 200, 0, 0
        self.bullets_allowed = 10

        self.fleet_drop_speed = 8
        self.ship_limit = 3
        self.speedup_scale = 1.5
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # speed factors
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 2
        # 1 for right, -1 for left
        self.fleet_direction = 1
        self.alien_points = 500

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.bullet_width += self.speedup_scale * 10

        self.alien_points = int(self.alien_points*self.score_scale)
