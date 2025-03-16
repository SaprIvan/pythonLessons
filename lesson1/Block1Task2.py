is_gun_ready = bool(input())
ammo_count = int(input())

should_fire = is_gun_ready and ammo_count > 0
print(should_fire)

