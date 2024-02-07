import pywhatkit as kit
import time


target_contact = "+57 305 3719299"

message_to_send = "Maldita sea."

repeat_count = 5

def send_troll_messages(target, message, repeat):
    for i in range(repeat):
        kit.sendwhatmsg_instantly(target, message)
        time.sleep(10)


send_troll_messages(target_contact, message_to_send, repeat_count)


