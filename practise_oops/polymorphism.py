class Messenger:
    def use_keyboard(self):
        print("Using keyboard")
    def send_message(self):
        print("text message sent")
    def receive_message(self):
        print("text message received")
class FbMessenger(Messenger):
    def send_message(self):
        print("Facebook message sent")
    def receive_message(self):
        print("Facebook message received")
        
def use_messenger(ref):
    ref.use_keyboard()
    ref.send_message()
    ref.receive_message()

m = Messenger()
fb = FbMessenger()
use_messenger(m)
use_messenger(fb)