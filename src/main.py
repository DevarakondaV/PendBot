from boot import do_connect
if (do_connect()):
    import control
else:
    print("Not Connected")
