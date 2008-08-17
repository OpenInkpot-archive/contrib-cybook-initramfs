dir /mnt 0755 0 0
dir /mnt/card 0755 0 0
dir /mnt/ext 0755 0 0

dir /newroot 0755 0 0
dir /dev 0755 0 0
dir /bin 0755 0 0
dir /sbin 0755 0 0
dir /lib 0755 0 0
dir /proc 0755 0 0
dir /sys 0755 0 0
dir /etc 0755 0 0

nod /dev/zero 0666 0 0 c 1 5
nod /dev/null 0666 0 0 c 1 3
nod /dev/loop0 0600 0 0 b 7 0
nod /dev/console 0666 0 0 c 5 1

nod /dev/sda1 0666 0 0 b 8 1
nod /dev/sda2 0666 0 0 b 8 2
nod /dev/sdb1 0666 0 0 b 8 17
nod /dev/sdb2 0666 0 0 b 8 18

nod /dev/tty 0666 0 0 c 5 0
nod /dev/tty0 0666 0 0 c 4 0
nod /dev/ptmx 0666 0 0 c 5 2
nod /dev/aio 0666 0 0 c 1 10
nod /dev/ttySAC0 0666 0 0 c 204 64

file /bin/busybox ./busybox 0755 0 0
file /init ./init 0755 0 0

slink /bin/[ /bin/busybox 0755 0 0
slink /bin/[[ /bin/busybox 0755 0 0
slink /bin/sh /bin/busybox 0755 0 0
slink /bin/mount /bin/busybox 0755 0 0
slink /bin/umount /bin/busybox 0755 0 0
slink /bin/losetup /bin/busybox 0755 0 0
slink /bin/echo /bin/busybox 0755 0 0
slink /bin/sleep /bin/busybox 0755 0 0
slink /bin/switch_root /bin/busybox 0755 0 0
