class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        self.screen_width = 800
        self.screen_hegiht = 600
        self.bg_color = (230, 230, 230)
        # 飞船的设置
        self.ship_speed_factor = 1.5