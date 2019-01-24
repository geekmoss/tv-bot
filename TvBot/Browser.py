from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys


class Browser:
    def __init__(self, webdriver=None, debug=False):
        if webdriver is None:
            from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

            cap = DesiredCapabilities().FIREFOX
            cap['args'] = ['--headless']
            cap["marionette"] = False

            webdriver = Firefox(capabilities=cap)
            pass

        self.__closed = False
        self.first_tab = True
        self.__fullscreen = False
        self.tabs = {}
        self.debug = debug
        self.f = webdriver
        pass

    def open(self, url):
        self.f.get(url)
        self.tabs[self.f.current_window_handle] = self.f.current_url

        return self.f.current_window_handle

    def open_in_new_tab(self, url):
        if self.first_tab:
            self.first_tab = False
            return self.open(url)

        self.f.execute_script(f"window.open('{url}', '_blank');")
        tab_id = self.next_tab()
        self.tabs[tab_id] = self.f.current_url

        return tab_id

    def close(self):
        for w in self.f.window_handles:
            self.switch_to_tab(w)
            self.f.close()
            pass
        self.__closed = True
        pass

    def next_tab(self):
        i = self.f.window_handles.index(self.f.current_window_handle)

        i = 0 if i == (len(self.f.window_handles) - 1) else (i + 1)

        self.f.switch_to.window(self.f.window_handles[i])

        return self.f.window_handles[i]

    def switch_to_tab(self, tab_id):
        self.f.switch_to.window(tab_id)
        pass

    def close_tab(self, tab_id):
        self.switch_to_tab(tab_id)
        self.f.close()
        self.switch_to_tab(self.f.window_handles[0])
        del self.tabs[tab_id]
        pass

    def toggle_fullscreen(self):
        if self.__fullscreen:
            self.f.maximize_window()
            pass
        else:
            self.f.fullscreen_window()
            pass
        pass

    def __del__(self):
        if hasattr(self, '__closed') and not self.__closed:
            self.f.close()
            pass
        pass
    pass
