class MusicPlayer:
    def __init__(self):
        self.head = None
        self.current = None
    # add song to circular doubly linked list
    def add_song(self, data):
        new = Song(data)  # node1=Node(9)

        if self.head is None:
            self.head = new
            new.next = new
            new.prev = new
            self.current = new
        else:
            tail = self.head.prev
            tail.next = new
            new.prev = tail
            new.next = self.head
            self.head.prev = new

    def play(self):
        if self.current:
            pygame.mixer.music.load(self.current.data)
            pygame.mixer.music.play()
            print("Playing:", self.current.data)

    def next_song(self):
        if self.current:
            self.current = self.current.next
            self.play()

    def prev_song(self):
        if self.current:
            self.current = self.current.prev
            self.play()


player = MusicPlayer()


# Add songs
player.add_song(r"C:\Users\VISHAL\OneDrive\Desktop\dsa_ASS\1.mp3")
player.add_song(r"C:\Users\VISHAL\OneDrive\Desktop\dsa_ASS\2.mp3")


while True:
    print("\n1.Play 2.Next 3.Previous 0.Exit")
    

    choice = int(input("Enter choice: "))

    if choice == 1:
        player.play()
    elif choice == 2:
        player.next_song()
    elif choice == 3:
        player.prev_song()
    elif choice == 0:
        pygame.mixer.music.stop()
        break
    else:
        print("Invalid choice")
