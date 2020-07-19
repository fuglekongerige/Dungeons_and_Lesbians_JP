# TODO: Translation updated at 2020-06-26 18:08

init python:
    config.language = "Japanese"



translate japanese style say_dialogue:
    language "japanese-normal"

translate Japanese python:
    gui.text_font = "tl/Japanese/mikachan.ttf"
    gui.name_text_font = "tl/Japanese/mikachan.ttf"
    gui.interface_text_font = "tl/Japanese/mikachan.ttf"
    gui.button_text_font = gui.interface_text_font
    gui.choice_button_text_font = gui.text_font

define non = Character(None, color="#593131",)
define cnon = Character(None, kind=nvl, color="#593131",)

define l = Character('レナ', color="#593131",)#Lenjamin
define r = Character('ラフィー', color="#593131",)#Giraffe
define g = Character('グウェン', color="#593131",)
define j = Character('ジモシー', color="#593131",)

define u = Character('あなた', color="#593131", )

define gm = Character('ゲームマスター', color="#593131",)
define hun = Character('ハンター', color="#593131",)
define pala = Character('パラディン', color="#593131",)
define a = Character('衛兵A', color="#593131",)

    
translate Japanese strings:

    # game/screens.rpy:256
    old "Back"
    new "もどる"

    # game/screens.rpy:257
    old "History"
    new "ログ"

    # game/screens.rpy:258
    old "Skip"
    new "スキップ"

    # game/screens.rpy:259
    old "Auto"
    new "オート"

    # game/screens.rpy:260
    old "Save"
    new "セーブ"

    # game/screens.rpy:261
    old "Q.Save"
    new "クイックセーブ"

    # game/screens.rpy:262
    old "Q.Load"
    new "クイックロード"

    # game/screens.rpy:263
    old "Prefs"
    new "設定"

    # game/screens.rpy:304
    old "      Start"
    new "スタート"

    # game/screens.rpy:312
    old "     Load"
    new "ロード"

    # game/screens.rpy:314
    old "Preferences"
    new "設定"

    # game/screens.rpy:318
    old "End Replay"
    new "End Replay"

    # game/screens.rpy:322
    old "Main Menu"
    new "メインメニュー"

    # game/screens.rpy:324
    old "  About"
    new "About"

    # game/screens.rpy:329
    old "   Help"
    new "ヘルプ"

    # game/screens.rpy:335
    old "Quit"
    new "終わる"

    # game/screens.rpy:476
    old "Return"
    new "もどる"

    # game/screens.rpy:553
    old "About"
    new "About"

    # game/screens.rpy:560
    old "Version [config.version!t]\n"
    new "Version [config.version!t]\n"

    # game/screens.rpy:566
    old "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"
    new "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"

    # game/screens.rpy:601
    old "Load"
    new "ロード"

    # game/screens.rpy:606
    old "Page {}"
    new "Page {}"

    # game/screens.rpy:606
    old "Automatic saves"
    new "オートセーブ"

    # game/screens.rpy:606
    old "Quick saves"
    new "クイックセーブ"

    # game/screens.rpy:648
    old "{#file_time}%A, %B %d %Y, %H:%M"
    new "{#file_time}%A, %B %d %Y, %H:%M"

    # game/screens.rpy:648
    old "empty slot"
    new "空きスロット"

    # game/screens.rpy:665
    old "<"
    new "<"

    # game/screens.rpy:668
    old "{#auto_page}A"
    new "{#auto_page}A"

    # game/screens.rpy:671
    old "{#quick_page}Q"
    new "{#quick_page}Q"

    # game/screens.rpy:677
    old ">"
    new ">"

    # game/screens.rpy:734
    old "Display"
    new "ディスプレイ"

    # game/screens.rpy:735
    old "Window"
    new "ウィンドウ"

    # game/screens.rpy:736
    old "Fullscreen"
    new "フルスクリーン"

    # game/screens.rpy:740
    old "Rollback Side"
    new "ロールバックの方向"

    # game/screens.rpy:741
    old "Disable"
    new "無効"

    # game/screens.rpy:742
    old "Left"
    new "左"

    # game/screens.rpy:743
    old "Right"
    new "右"

    # game/screens.rpy:748
    old "Unseen Text"
    new "未読テキスト"

    # game/screens.rpy:749
    old "After Choices"
    new "選択肢の後"

    # game/screens.rpy:750
    old "Transitions"
    new "場面転換"

    # game/screens.rpy:763
    old "Text Speed"
    new "文字送り速度"

    # game/screens.rpy:767
    old "Auto-Forward Time"
    new "オートで進む速度"

    # game/screens.rpy:774
    old "Music Volume"
    new "音楽の音量"

    # game/screens.rpy:781
    old "Sound Volume"
    new "効果音の音量"

    # game/screens.rpy:787
    old "Test"
    new "テスト"

    # game/screens.rpy:791
    old "Voice Volume"
    new "声の音量"

    # game/screens.rpy:802
    old "Mute All"
    new "すべてミュート"

    # game/screens.rpy:921
    old "The dialogue history is empty."
    new "表示するログがありません。"

    # game/screens.rpy:982
    old "Help"
    new "ヘルプ"

    # game/screens.rpy:991
    old "Keyboard"
    new "キーボード"

    # game/screens.rpy:992
    old "Mouse"
    new "マウス"

    # game/screens.rpy:995
    old "Gamepad"
    new "コントローラー"

    # game/screens.rpy:1008
    old "Enter"
    new "Enter"

    # game/screens.rpy:1009
    old "Advances dialogue and activates the interface."
    new "ダイアログの読み進め、インターフェイスの有効化"

    # game/screens.rpy:1012
    old "Space"
    new "Space"

    # game/screens.rpy:1013
    old "Advances dialogue without selecting choices."
    new "ダイアログの読み進め（選択肢は選択しない）"

    # game/screens.rpy:1016
    old "Arrow Keys"
    new "Arrow Keys"

    # game/screens.rpy:1017
    old "Navigate the interface."
    new "インターフェイスの操作"

    # game/screens.rpy:1020
    old "Escape"
    new "Escape"

    # game/screens.rpy:1021
    old "Accesses the game menu."
    new "メニューにアクセス"

    # game/screens.rpy:1024
    old "Ctrl"
    new "Ctrl"

    # game/screens.rpy:1025
    old "Skips dialogue while held down."
    new "押している間ダイアログをスキップ"

    # game/screens.rpy:1028
    old "Tab"
    new "Tab"

    # game/screens.rpy:1029
    old "Toggles dialogue skipping."
    new "ダイアログのスキップの仕方をトグル"

    # game/screens.rpy:1032
    old "Page Up"
    new "Page Up"

    # game/screens.rpy:1033
    old "Rolls back to earlier dialogue."
    new "前のダイアログに戻る"

    # game/screens.rpy:1036
    old "Page Down"
    new "Page Down"

    # game/screens.rpy:1037
    old "Rolls forward to later dialogue."
    new "後のダイアログへ進む"

    # game/screens.rpy:1041
    old "Hides the user interface."
    new "インターフェイスを隠す"

    # game/screens.rpy:1045
    old "Takes a screenshot."
    new "スクリーンショットを撮る"

    # game/screens.rpy:1049
    old "Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}."
    new "{a=https://www.renpy.org/l/voicing}セルフボイシング{/a}機能をトグル"

    # game/screens.rpy:1055
    old "Left Click"
    new "左クリック"

    # game/screens.rpy:1059
    old "Middle Click"
    new "ホイールクリック"

    # game/screens.rpy:1063
    old "Right Click"
    new "右クリック"

    # game/screens.rpy:1067
    old "Mouse Wheel Up\nClick Rollback Side"
    new "ホイール（上）\nロールバックで設定した方向をクリック"


    # game/screens.rpy:1071
    old "Mouse Wheel Down"
    new "ホイール（下）"

    # game/screens.rpy:1078
    old "Right Trigger\nA/Bottom Button"
    new "Right Trigger\nA/Bottom Button"

    # game/screens.rpy:1082
    old "Left Trigger\nLeft Shoulder"
    new "Left Trigger\nLeft Shoulder"

    # game/screens.rpy:1086
    old "Right Shoulder"
    new "Right Shoulder"

    # game/screens.rpy:1091
    old "D-Pad, Sticks"
    new "D-Pad, Sticks"

    # game/screens.rpy:1095
    old "Start, Guide"
    new "Start, Guide"

    # game/screens.rpy:1099
    old "Y/Top Button"
    new "Y/Top Button"

    # game/screens.rpy:1102
    old "Calibrate"
    new "Calibrate"

    # game/screens.rpy:1168
    old "No"
    new "いいえ"

    # game/screens.rpy:1214
    old "Skipping"
    new "Skipping"

    # game/screens.rpy:1437
    old "Menu"
    new "Menu"

