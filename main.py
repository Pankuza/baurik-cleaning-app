from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex
from kivy.metrics import dp
import webbrowser

class BaurikApp(App):
    def build(self):
        scroll = ScrollView()
        main_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15), size_hint_y=None)
        main_layout.bind(minimum_height=main_layout.setter('height'))
        
        with main_layout.canvas.before:
            Color(*get_color_from_hex('#2c5aa0'))
            self.rect = Rectangle(size=main_layout.size, pos=main_layout.pos)
        
        header = Label(
            text='[b]✨ BAURIK CLEANING SOLUTIONS ✨[/b]',
            markup=True,
            font_size='24sp',
            size_hint_y=None,
            height=dp(70),
            color=get_color_from_hex('#ffffff'),
            halign='center'
        )
        
        tagline = Label(
            text='Professional Cleaning Services • Since 2023',
            font_size='16sp',
            size_hint_y=None,
            height=dp(30),
            color=get_color_from_hex('#ffffff'),
            halign='center'
        )
        
        contact_header = Label(
            text='[b]📞 CONTACT US[/b]',
            markup=True,
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            color=get_color_from_hex('#ffffff'),
            halign='center'
        )
        
        phone_btn = Button(
            text='📞 CALL: 061 737 0031',
            size_hint_y=None,
            height=dp(60),
            background_color=get_color_from_hex('#4CAF50'),
            background_normal='',
            on_press=self.call_number
        )
        
        email_btn = Button(
            text='✉️ EMAIL: baurikcleaningsolutions@gmail.com',
            size_hint_y=None,
            height=dp(60),
            background_color=get_color_from_hex('#FF9800'),
            background_normal='',
            on_press=self.send_email
        )
        
        website_btn = Button(
            text='🌐 VISIT OUR WEBSITE',
            size_hint_y=None,
            height=dp(60),
            background_color=get_color_from_hex('#2196F3'),
            background_normal='',
            on_press=self.open_website
        )
        
        quote_header = Label(
            text='[b]📧 REQUEST QUOTE[/b]',
            markup=True,
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            color=get_color_from_hex('#ffffff'),
            halign='center'
        )
        
        self.name_input = TextInput(
            hint_text='Your Full Name *',
            size_hint_y=None,
            height=dp(50)
        )
        
        self.phone_input = TextInput(
            hint_text='Your Phone Number *',
            size_hint_y=None,
            height=dp(50),
            input_type='phone'
        )
        
        self.email_input = TextInput(
            hint_text='Your Email Address',
            size_hint_y=None,
            height=dp(50)
        )
        
        service_layout = BoxLayout(size_hint_y=None, height=dp(50))
        service_layout.add_widget(Label(text='Service:', size_hint_x=0.3, color=get_color_from_hex('#ffffff')))
        self.service_spinner = Spinner(
            text='Choose Service',
            values=('Residential Cleaning', 'Office Cleaning', 'Deep Cleaning', 'Window Cleaning', 'Carpet Cleaning', 'Move-In/Move-Out'),
            size_hint_x=0.7
        )
        service_layout.add_widget(self.service_spinner)
        
        self.message_input = TextInput(
            hint_text='Additional details...',
            size_hint_y=None,
            height=dp(80),
            multiline=True
        )
        
        self.submit_btn = Button(
            text='🚀 SEND QUOTE REQUEST',
            size_hint_y=None,
            height=dp(70),
            background_color=get_color_from_hex('#2c5aa0'),
            background_normal='',
            on_press=self.submit_quote
        )
        
        main_layout.add_widget(header)
        main_layout.add_widget(tagline)
        main_layout.add_widget(contact_header)
        main_layout.add_widget(phone_btn)
        main_layout.add_widget(email_btn)
        main_layout.add_widget(website_btn)
        main_layout.add_widget(quote_header)
        main_layout.add_widget(self.name_input)
        main_layout.add_widget(self.phone_input)
        main_layout.add_widget(self.email_input)
        main_layout.add_widget(service_layout)
        main_layout.add_widget(self.message_input)
        main_layout.add_widget(self.submit_btn)
        
        scroll.add_widget(main_layout)
        return scroll
    
    def call_number(self, instance):
        webbrowser.open('tel:0617370031')
    
    def send_email(self, instance):
        webbrowser.open('mailto:baurikcleaningsolutions@gmail.com')
    
    def open_website(self, instance):
        webbrowser.open('https://baurikcleaning.great-site.net/landing-page')
    
    def submit_quote(self, instance):
        name = self.name_input.text.strip()
        phone = self.phone_input.text.strip()
        email = self.email_input.text.strip()
        service = self.service_spinner.text
        message = self.message_input.text.strip()
        
        if not name or not phone:
            instance.text = '❌ PLEASE FILL REQUIRED FIELDS!'
            instance.background_color = get_color_from_hex('#FF0000')
            Clock.schedule_once(lambda dt: self.reset_button(instance), 2)
            return
        
        subject = f"Quote Request: {service}"
        body = f"""Name: {name}
Phone: {phone}
Email: {email}
Service: {service}
Message: {message}

Sent via Baurik Cleaning Solutions Mobile App"""
        
        webbrowser.open(f"mailto:baurikcleaningsolutions@gmail.com?subject={subject}&body={body}")
        
        self.name_input.text = ''
        self.phone_input.text = ''
        self.email_input.text = ''
        self.message_input.text = ''
        
        instance.text = '✅ QUOTE SENT! CHECK EMAIL APP'
        instance.background_color = get_color_from_hex('#388E3C')
        Clock.schedule_once(lambda dt: self.reset_button(instance), 3)
    
    def reset_button(self, button):
        button.text = '🚀 SEND QUOTE REQUEST'
        button.background_color = get_color_from_hex('#2c5aa0')

if __name__ == '__main__':
    BaurikApp().run()
