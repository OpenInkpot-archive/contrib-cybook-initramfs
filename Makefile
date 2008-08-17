all: initrd.igz

initrd.igz: initramfs.spec busybox init busybox-1.8.2.config
	/usr/src/linux/usr/gen_init_cpio initramfs.spec | gzip > initrd.igz

clean:
	rm initrd.igz
