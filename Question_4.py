class TVClass:
    def __init__(self, brand, price, inches, on_off_status):
        self.brand = brand
        self.channel = 1
        self.price = price
        self.inches = inches
        self.on_off_status = on_off_status
        self.volume = 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel
        else:
            print("This is the last channel available")

    def reset_mode(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LED(TVClass):
    def __init__(self, brand, price, inches, on_off_status, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight):
        super().__init__(brand, price, inches, on_off_status)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        return f"LED TV - Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, " \
               f"Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}, Viewing Angle: {self.viewing_angle}, Backlight: {self.backlight}"


class Plasma(TVClass):
    def __init__(self, brand, price, inches, on_off_status, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight):
        super().__init__(brand, price, inches, on_off_status)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        return f"Plasma TV - Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, " \
               f"Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}, Viewing Angle: {self.viewing_angle}, Backlight: {self.backlight}"


led_tv = LED("Sony", "$300", "42 inches", "Off", "5mm", "50W", "10 years", "120Hz", "170 degrees", "Edge-lit")
plasma_tv = Plasma("LG", "$250", "45 inches", "Off", "6mm", "70W", "15 years", "60Hz", "180 degrees", "3D")

print(led_tv.status())
led_tv.increase_volume()
led_tv.set_channel(45)
print(led_tv.status())
print(led_tv.display_details())

print(plasma_tv.status())
plasma_tv.decrease_volume()
plasma_tv.set_channel(60)  
print(plasma_tv.status())
print(plasma_tv.display_details())
