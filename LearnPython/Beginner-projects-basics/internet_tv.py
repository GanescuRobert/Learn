

class NetworkDevice:
    def __init__(self, mac_no, cache_size):
        self.mac_no = mac_no
        self.cache_size = cache_size

    def transmit(self):
        print('Requestin a download ...')

    def receive(self, data_size):
        if data_size > self.cache_size:
            print('Receipt aborted: packet size too large.')
            return False
        else:
            print('Received data packets.')
            return True


class Television:
    def __init__(self, screen, volume_tuner):
        self.screen = screen
        self.volume_tuner = volume_tuner

    def display_video(self):
        print('Displaying video on a ' + self.screen)

    def change_volume(self, amount):
        if amount < 0:
            print('Reducing sound by ' + str(-amount) + ' unit(s).')
        if amount > 0:
            print('Increasing sound by ' + str(amount) + ' units(s).')


class InternetTv(Television, NetworkDevice):
    def __init__(self, screen, volume_tuner, mac_no, cache_size, cpu):
        self.cpu=cpu
        NetworkDevice.__init__(self, mac_no,cache_size)
        Television.__init__(self, screen, volume_tuner)
    def watch_network_tv(self,data_size):
        NetworkDevice.transmit(self)
        is_received = NetworkDevice.receive(self,data_size)
        if is_received:
            Television.display_video(self)

a_tv = InternetTv('LED screen', 'digital tuner', '789-345', 2, 'qualcomm')
a_tv.watch_network_tv(1)
a_tv.change_volume(-1)
a_tv.watch_network_tv(3)