from flask_socketio import Namespace, emit
from click import echo, style


class Socket(Namespace):
    def __init__(self, namespace, debug):
        super().__init__(namespace)
        self.tabs = []
        self.debug = debug
        pass

    def on_connect(self):
        if self.debug:
            echo(style("CONNECT", fg="bright_black"))
            pass
        return self.tabs

    def on_disconnect(self):
        if self.debug:
            echo(style("DISCONNECT", fg="bright_black"))
            pass
        pass

    def on_ls_return(self):
        if self.debug:
            echo("LS Return")
            pass

        return self.tabs

    def on_ls(self):
        if self.debug:
            echo("LS")
            pass

        emit('ls', self.tabs)
        pass

    def on_put(self, url):
        if self.debug:
            echo(f"{style('PUT', fg='green')} {url} -> EMIT LS, Broadcast=True")
            pass

        if url not in self.tabs:
            self.tabs.append(url)
            emit('ls', self.tabs, broadcast=True)
            pass
        pass

    def on_del(self, url):
        if self.debug:
            echo(f"{style('DEL', fg='red')} {url} -> EMIT LS, Broadcast=True")
            pass

        if url in self.tabs:
            self.tabs.remove(url)
            pass

        emit('ls', self.tabs, broadcast=True)
        pass

    def on_nextTab(self):
        if self.debug:
            echo(f"{style('NEXT TAB', fg='blue')} -> EMIT NEXT TAB, Broadcast=True")
            pass
        emit('nextTab', broadcast=True)
        pass

    def on_prevTab(self):
        if self.debug:
            echo(f"{style('PREV TAB', fg='blue')} -> EMIT PREV TAB, Broadcast=True")
            pass
        emit('prevTab', broadcast=True)
        pass

    def on_fullscreen(self):
        if self.debug:
            echo(f"{style('FULLSCREEN', fg='blue')} -> EMIT FULLSCREEN, Broadcast=True")
            pass
        emit('fullscreen', broadcast=True)
        pass
    pass
