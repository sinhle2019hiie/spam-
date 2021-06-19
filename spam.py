import pyautogui, time, pyperclip

s = int(input("Số lần muốn spam: "))
n = input("Nội dung spam: ")
d = int(input("Nhập thời gian delay: "))
print("Đợi trong ", d, "giây")
time.sleep(d)

for i in range(s):
    pyperclip.copy(n)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    