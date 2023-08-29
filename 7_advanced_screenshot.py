import time
import keyboard
from PIL import ImageGrab


def screenshot():  #-->(1)실행은 이미지그랩에서 그랩으로 이미지를 가져와서 img에 저장하되...
    # 2023년 7월 7일 14시 20분 17초--> _20230707_142017
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))  #...이러한 형식으로 저장한다...
                    # ex) image _20230707_142017.png


keyboard.add_hotkey("F9", screenshot) # F9를 눌렀을때 스크린샷을 실행-->(1)
# keyboard.add_hotkey("a", screenshot)
# keyboard.add_hotkey("ctrl+shift+s", screenshot)

keyboard.wait("esc") # 사용자가 esc를 누를 떄까지 프로그램 수행