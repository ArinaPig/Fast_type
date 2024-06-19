# import keyboard
#
# print("Нажмите любую клавишу:")
# key_pressed = keyboard.read_event()
# if key_pressed.event_type == keyboard.KEY_DOWN:
#    print("Вы нажали клавишу:", key_pressed.name)

import keyboard

print("Нажмите любую клавишу:")
key_pressed = keyboard.read_event()

if key_pressed.event_type == keyboard.KEY_DOWN and key_pressed.name == 'space':
   print('Вы нажали верную клавишу')
elif key_pressed.event_type == keyboard.KEY_DOWN and key_pressed.name != 'space':
   print('неверно')
   key_pressed = keyboard.read_event()


