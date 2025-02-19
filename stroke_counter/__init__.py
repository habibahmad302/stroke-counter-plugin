import wx
import plover.plugin
from plover.gui.util import Toolbox

class StrokeCounterGUI(Toolbox):
    def __init__(self, engine, parent):
        super().__init__(parent, 'Stroke Counter')
        self.engine = engine
        self.count = 0

        panel = wx.Panel(self)
        self.label = wx.StaticText(panel, label='Strokes: 0')
        reset_button = wx.Button(panel, label='Reset Counter')

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.label, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(reset_button, 0, wx.ALL | wx.CENTER, 10)
        panel.SetSizer(sizer)

        reset_button.Bind(wx.EVT_BUTTON, self.on_reset)
        self._parent = parent
        self.Show()

    def on_reset(self, event):
        self.count = 0
        self.label.SetLabel('Strokes: 0')

    def increment_count(self):
        self.count += 1
        self.label.SetLabel(f'Strokes: {self.count}')

class StrokeCounter(plover.plugin.Plugin):
    def __init__(self, engine):
        super().__init__(engine)
        self.gui = None

    def start(self):
        self.engine.signal_connect('stroked', self.on_stroke)
        if self.engine.gui:
            self.gui = StrokeCounterGUI(self.engine, self.engine.gui.main_window)

    def on_stroke(self, stroke):
        if self.gui:
            wx.CallAfter(self.gui.increment_count)

    def stop(self):
        self.engine.signal_disconnect('stroked', self.on_stroke)
        if self.gui:
            self.gui.Destroy()
            self.gui = None
