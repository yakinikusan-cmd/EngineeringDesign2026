import wheel_control
class Map:
    def __init__(self):
        self.chars = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","　","ゆ","　","よ","ら","り","る","れ","ろ","わ","　","　","　","を","ん"]
        self.box_width = 50
        self.box_height = 50

    def get_pos_by_letter(self,char):
        try:
            index = self.chars.index(char)
        except ValueError:
            print("enter valid charactor")
            return -1
        
        q, mod = divmod(index + 1, 5)
        mod -= 1 #ゼロインデックスに合わせる
        pos = wheel_control.Position()
        pos.x = (q * self.box_width) + (self.box_width / 2)
        pos.y = (q * self.box_height) + (self.box_height / 2)
        return pos
    def print_chars(self):
        for i in range(len(self.chars)):
            print(self.chars[i],end=" ")
            if (i + 1) % 5 == 0:
                print()
        print()

map = Map()
map.print_chars()
map.get_pos_by_letter("ゆ")