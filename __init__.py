"""Soft Theme: Anki のメイン画面・ツールバー・ボタンを見やすくする CSS を差し込む。"""
from aqt import mw, gui_hooks
from aqt.deckbrowser import DeckBrowser, DeckBrowserBottomBar
from aqt.overview import Overview, OverviewBottomBar
from aqt.toolbar import TopToolbar, BottomToolbar
from aqt.reviewer import ReviewerBottomBar

ADDON = __name__.split(".")[0]
mw.addonManager.setWebExports(__name__, r"web/.*\.css")
CSS = f"/_addons/{ADDON}/web/theme.css"

TARGETS = {
    DeckBrowser: "st-decks",
    Overview: "st-overview",
    TopToolbar: "st-toolbar",
    BottomToolbar: "st-bottombar",
    DeckBrowserBottomBar: "st-bottombar",
    OverviewBottomBar: "st-bottombar",
    ReviewerBottomBar: "st-reviewbar",
}


def on_set_content(web_content, context):
    for cls, page in TARGETS.items():
        if isinstance(context, cls):
            web_content.css.append(CSS)
            web_content.head += (
                f"<script>document.addEventListener('DOMContentLoaded',"
                f"()=>document.body.classList.add('st','{page}'));</script>"
            )
            return


gui_hooks.webview_will_set_content.append(on_set_content)


# ---------- ウィンドウの透明度 ----------
def apply_opacity(*_args):
    conf = mw.addonManager.getConfig(__name__) or {}
    try:
        value = float(conf.get("window_opacity", 1.0))
    except (TypeError, ValueError):
        value = 1.0
    mw.setWindowOpacity(min(1.0, max(0.3, value)))


gui_hooks.main_window_did_init.append(apply_opacity)
mw.addonManager.setConfigUpdatedAction(__name__, apply_opacity)
