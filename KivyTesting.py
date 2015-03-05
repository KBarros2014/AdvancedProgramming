'''
Widget animation
================

This is an example of an animation creation, and how you can apply it to a
widget.
'''

import kivy
kivy.require('1.0.7')

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):

    def animate(self, instance):
        # create an animation object. 
        animation = Animation(pos=(100, 300), t='out_bounce')
        animation += Animation(pos=(230, 100), t='out_bounce')
        animation &= Animation(size=(200, 600))
        animation += Animation(size=(100, 50))

        # apply the animation on the button, passed in the "instance" argument
        animation.start(instance)

    def build(self):
        # create a button, and  attach animate() method as a on_press handler
        button = Button(size_hint=(None, None), text='hello world', on_press=self.animate)
        return button

if __name__ == '__main__':
    TestApp().run()
