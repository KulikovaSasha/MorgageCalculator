from kivy.lang import Builder
from kivy.properties import StringProperty, ColorProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawerItem, MDNavigationDrawerItemTrailingText
)

from kivymd.uix.label import MDLabel
from kivymd.uix.tab import (
    MDTabsItemIcon,
    MDTabsItemText,
    MDTabsItem,
)

from kivymd.font_definitions import fonts

KV = '''
<DrawerItem>
    active_indicator_color: "#4a4939"

    MDNavigationDrawerItemLeadingIcon:
        icon: root.icon
        theme_icon_color: "Custom"
        icon_color: "#4a4939"

    MDNavigationDrawerItemText:
        text: root.text
        theme_text_color: "Custom"
        text_color: "#4a4939"


<DrawerLabel>
    adaptive_height: True
    padding: "18dp", 0, 0, "12dp"

    MDNavigationDrawerItemLeadingIcon:
        icon: root.icon
        theme_icon_color: "Custom"
        icon_color: "#4a4939"
        pos_hint: {"center_y": .5}

    MDNavigationDrawerLabel:
        text: root.text
        theme_text_color: "Custom"
        text_color: "#4a4939"
        pos_hint: {"center_y": .5}
        padding: "6dp", 0, "16dp", 0
        theme_line_height: "Custom"
        line_height: 0


MDScreen:

    md_bg_color: self.theme_cls.backgroundColor

    MDTabsPrimary:

        id: tabs
        md_bd_color: 0, 0, 0, 1
        allow_stretch: True
        pos_hint: {"center_x": .5, "center_y": .5}
        #size_hint_x: .5
        #label_only: True

        MDDivider:

        MDTabsCarousel:
            id: related_content_container
            size_hint_y: None
            height: root.height - tabs.ids.tab_scroll.height       
            background_color: 0.1, 0.1, 0.1, 1
    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDButton:
                    size_hint_y: None
                 
                    #pos_hint: {"left_x": 0, "center_y": 0.965}
                    on_release: nav_drawer.set_state("toggle")

                    MDButtonText:
                        text: "Menu"
                        
                        
                        


        MDNavigationDrawer:
            id: nav_drawer
            radius: 0, dp(16), dp(16), 0

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    orientation: "vertical"
                    padding: 0, 0, 0, "12dp"
                    adaptive_height: True

                    MDLabel:
                        text: app.title
                        theme_text_color: "Custom"
                        theme_line_height: "Custom"
                        line_height: 0
                        text_color: "#4a4939"
                        adaptive_height: True
                        adaptive_width: True
                        padding_x: "15dp"
                        font_style: "Title"
                        role: "large"

                    MDLabel:
                        text: app.by_who
                        padding_x: "4dp"
                        adaptive_height: True
                        adaptive_width: True
                        font_style: "Title"
                        role: "small"

                MDNavigationDrawerDivider:

                DrawerItem:
                    icon: "account-circle"
                    
                    text: "About author"
                    #trailing_text: "+99"
                    #trailing_text_color: "#d43e19"

                MDNavigationDrawerDivider:

                DrawerItem:
                    icon: "instagram"
                    text: "My instagram"

                MDNavigationDrawerDivider:

                DrawerItem:
                    icon: "coffee"
                    text: "Donate author"

                MDNavigationDrawerDivider:

                DrawerItem:
                    icon: "github"
                    text: "Source code"

                MDNavigationDrawerDivider:

                DrawerItem:
                    icon: "share-variant"
                    text: "Share app"

                MDNavigationDrawerDivider:

                DrawerItem:
                    icon: "shield-sun"
                    text: "Dark/Light"

                MDNavigationDrawerDivider:

                #MDNavigationDrawerLabel:
                    #text: "Labels"
                    #padding_y: "12dp"

                #DrawerLabel:
                    #icon: "information-outline"
                    #text: "Label"
                    
        
                    
                

'''


class DrawerLabel(MDBoxLayout):
    icon = StringProperty()
    text = StringProperty()



class DrawerItem(MDNavigationDrawerItem):
    icon = StringProperty()
    text = StringProperty()
    trailing_text = StringProperty()
    trailing_text_color = ColorProperty()

    _trailing_text_obj = None

    '''def on_trailing_text(self, instance, value):
        self._trailing_text_obj = MDNavigationDrawerItemTrailingText(
            text=value,
            theme_text_color="Custom",
            text_color=self.trailing_text_color,
        )
        self.add_widget(self._trailing_text_obj)'''

    '''def on_trailing_text_color(self, instance, value):
        self._trailing_text_obj.text_color = value'''


class MortgageCalculator(MDApp):
    title = "Mortgage Calculator"
    by_who = "author Alexandra Kulikova"

    def on_start(self):
        for tab_icon, tab_name in {
            "calculator-variant": "Input",  # ab-testing
            "table-large": "Table",
            "chart-areaspline": "Graph",
            "chart-pie": "Chart",  # chart-arc
            "book-open-variant": "Sum",

        }.items():
            self.root.ids.tabs.add_widget(
                MDTabsItem(
                    MDTabsItemIcon(
                        icon=tab_icon,
                    ),
                    MDTabsItemText(
                        text=tab_name,
                    ),
                )
            )
            self.root.ids.related_content_container.add_widget(
                MDLabel(
                    text=tab_name,
                    halign="center",
                )
            )
            self.root.ids.tabs.switch_tab(icon="airplane")

    def build(self):

        return Builder.load_string(KV)


MortgageCalculator().run()