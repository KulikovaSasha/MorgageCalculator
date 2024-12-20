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
    active_indicator_color: "#e7e4c0"

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
        pos_hint: {"center_x": .5, "center_y": .6}
        size_hint_x: 1
                
        MDDivider:
                
        MDTabsCarousel:
            id: related_content_container
            size_hint_y: None
            height: dp(320)        

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDButton:
                    pos_hint: {"left_x": 0, "center_y": 0.965}
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
                        text: "MC"
                        theme_text_color: "Custom"
                        theme_line_height: "Custom"
                        line_height: 0
                        text_color: "#4a4939"
                        adaptive_height: True
                        padding_x: "16dp"
                        font_style: "Display"
                        role: "small"

                    MDLabel:
                        text: "Header text"
                        padding_x: "18dp"
                        adaptive_height: True
                        font_style: "Title"
                        role: "large"

                MDNavigationDrawerDivider:

                DrawerItem:
                    icon: "folder"
                    text: "My files"
                    #trailing_text: "+99"
                    #trailing_text_color: "#4a4939"
                    
                MDNavigationDrawerDivider:

                DrawerItem:
                    icon: "account-multiple"
                    text: "Shared with me"

                MDNavigationDrawerDivider:
                
                DrawerItem:
                    icon: "star"
                    text: "Starred"

                MDNavigationDrawerDivider:
                
                DrawerItem:
                    icon: "history"
                    text: "Resent"

                MDNavigationDrawerDivider:
                
                DrawerItem:
                    icon: "checkbox-marked"
                    text: "Shared with me"

                MDNavigationDrawerDivider:
                
                DrawerItem:
                    icon: "upload"
                    text: "Upload"

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

    def on_trailing_text(self, instance, value):
        self._trailing_text_obj = MDNavigationDrawerItemTrailingText(
            text=value,
            theme_text_color="Custom",
            text_color=self.trailing_text_color,
        )
        self.add_widget(self._trailing_text_obj)

    def on_trailing_text_color(self, instance, value):
        self._trailing_text_obj.text_color = value


class MortgageCalculator(MDApp):
    def on_start(self):
        for tab_icon, tab_name in {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
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